import { useState, type FormEvent } from 'react'
import {
    Check, CheckCheck,
    Code2, FolderKanban, GitBranch,
} from 'lucide-react'
import {
    activity,
    formatDate,
    initialTasks,
    projectAppearance,
    projects,
} from './data/mockdata'
import { SidebarComponent } from '@/dashboard/components/Sidebar'
import { Topbar } from '@/dashboard/components/Topbar'
import { PageHeading } from '@/dashboard/components/PageHeading'
import { StatsGrid } from '@/dashboard/components/StatsGrid'
import { ProjectCard } from '@/dashboard/components/ProjectCard'
import { ProjectsSection } from '@/dashboard/components/ProjectsSection'
import { TaskRow } from '@/dashboard/components/TaskRow'
import { TasksSection } from '@/dashboard/components/TasksSection'
import { ProductivityChart } from '@/dashboard/components/ProductivityChart'
import { RecentActivity } from '@/dashboard/components/RecentActivity'
import { CustomFooter } from '@/components/custom/CustomFooter'
import { DashboardDialogs } from '@/dashboard/components/DashboardDialogs'

/* -------------------------------------------------------------------------- */
/*  Constantes de presentación                                                */
/* -------------------------------------------------------------------------- */






const today = () => new Date().toISOString().slice(0, 10)

/* -------------------------------------------------------------------------- */
/*  Componente                                                                */
/* -------------------------------------------------------------------------- */

export function Dashboard() {
    // ---------- Estado ----------
    const [tasks, setTasks] = useState(initialTasks)
    const [search, setSearch] = useState('')
    const [project, setProject] = useState('')            // id del proyecto seleccionado
    const [filter, setFilter] = useState('Todas')
    const [dialog, setDialog] = useState<'task' | 'notifications' | 'help' | null>(null)
    const [newName, setNewName] = useState('')
    const [newProject, setNewProject] = useState(projects[0]?.id ?? '')

    // ---------- Helpers ----------
    const getProjectName = (projectId: string) =>
        projects.find(p => p.id === projectId)?.name ?? 'Proyecto no disponible'

    const matchesSearch = (text: string) =>
        text.toLowerCase().includes(search.toLowerCase())

    // ---------- Datos derivados ----------
    const selectedProject = projects.find(p => p.id === project)
    const completed = tasks.filter(t => t.status === 'done').length
    const pendingTasks = tasks.filter(t => t.status !== 'done')

    const projectViews = projects.map(p => {
        const appearance = projectAppearance.find(item => item.projectId === p.id)
        const projectTasks = tasks.filter(t => t.projectId === p.id)
        const completedTasks = projectTasks.filter(t => t.status === 'done').length
        const nextDate =
            projectTasks
                .filter(t => t.status !== 'done' && t.date)
                .map(t => t.date)
                .sort()[0] ?? null

        return {
            ...p,
            tone: appearance?.tone ?? '',
            icon: appearance?.icon ?? Code2,
            initials: appearance?.initials ?? [],
            total: projectTasks.length,
            completed: completedTasks,
            progress: projectTasks.length
                ? Math.round((completedTasks / projectTasks.length) * 100)
                : 0,
            nextDate,
        }
    })

    const visibleProjects = projectViews.filter(p => {
        const matchesProject = !project || p.id === project
        const matchesText =
            !search ||
            matchesSearch(`${p.name} ${p.description}`) ||
            tasks.some(t => t.projectId === p.id && matchesSearch(t.title))
        return matchesProject && matchesText
    })

    const visibleTasks = tasks.filter(t => {
        const matchesProject = !project || t.projectId === project
        const matchesFilter =
            filter === 'Todas' ||
            (filter === 'Pendientes' && t.status !== 'done') ||
            (filter === 'Completadas' && t.status === 'done')
        const matchesText = matchesSearch(`${t.title} ${getProjectName(t.projectId)}`)
        return matchesProject && matchesFilter && matchesText
    })

    const visibleActivity = activity.filter(
        a => !selectedProject || a.project === selectedProject.name,
    )



    const stats = [
        {
            label: 'Proyectos activos',
            value: String(projects.filter(p => p.status === 'active').length),
            icon: FolderKanban, tone: '', note: 'Todos en marcha', change: '+1',
        },
        {
            label: 'Tareas pendientes',
            value: String(pendingTasks.length),
            icon: CheckCheck, tone: 'blue', note: 'asignadas a ti', change: 'Por completar',
        },
        {
            label: 'Tareas completadas',
            value: String(completed),
            icon: Check, tone: '', note: 'del total de tareas',
            change: `${tasks.length ? Math.round((completed / tasks.length) * 100) : 0}%`,
        },
        {
            label: 'Tareas con fecha',
            value: String(pendingTasks.filter(t => t.date).length),
            icon: GitBranch, tone: 'amber', note: 'pendientes', change: 'Programadas',
        },
    ]

    // ---------- Acciones ----------

    const toggleProject = (id: string) => setProject(project === id ? '' : id)


    const createTask = (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault()
        if (!newName.trim()) return

        setTasks([
            ...tasks,
            {
                id: crypto.randomUUID(),
                title: newName.trim(),
                projectId: newProject,
                priority: 'medium',
                date: today(),
                status: 'todo',
            },
        ])
        setNewName('')
        setDialog(null)
    }

    // ---------- Render ----------
    return (
        <div className="app-layout">
            {/* ===================== Sidebar ===================== */}
            <SidebarComponent projects={projectViews}
                project={project}
                onProjectChange={setProject}
                onSearchReset={() => setSearch('')}
                onOpenHelp={() => setDialog("help")} />

            <div className="main-column">
                {/* ===================== Topbar ===================== */}
                <Topbar search={search}
                    onSearchChanged={setSearch}
                    onOpenNotifications={() => setDialog('notifications')} />

                <main className="content">
                    {/* ===================== Encabezado ===================== */}
                    <PageHeading onNewTask={() => setDialog('task')} />

                    {/* ===================== Estadísticas ===================== */}
                    <StatsGrid stats={stats} />

                    {/* ===================== Proyectos ===================== */}
                    <section>
                        <ProjectsSection selectedProject={selectedProject}
                            project={project}
                            visibleProjects={visibleProjects}
                            onSetProject={setProject} />

                        <div className="project-grid">
                            {visibleProjects.map(project => {

                                return (
                                    <ProjectCard key={project.id}
                                        project={project}
                                        onSetProject={setProject} />
                                )
                            })}
                        </div>
                        {!visibleProjects.length && <p className="subtext mb-6">No se encontraron proyectos.</p>}
                    </section>

                    <div className="lower-grid">
                        <section>
                            {/* ===================== Tareas ===================== */}
                            <TasksSection tasks={visibleTasks} filter={filter} onSetFilter={setFilter} />

                            <div className="task-table">
                                {visibleTasks.map(t => {
                                    return (
                                        <TaskRow key={t.id}
                                            task={t}
                                            projectName={getProjectName(t.projectId)}
                                            onToggle={toggleProject} />
                                    )
                                })}
                                {!visibleTasks.length && (
                                    <p className="subtext p-6 text-center">No hay tareas en esta vista.</p>
                                )}
                            </div>

                            {/* ===================== Productividad ===================== */}
                            <ProductivityChart completed={completed} />
                        </section>

                        {/* ===================== Actividad reciente ===================== */}
                        <RecentActivity activities={visibleActivity} />
                    </div>

                    <CustomFooter leftMessage='Un paso a la vez. Cada commit cuenta' />
                </main>
            </div>

            {/* ===================== Diálogo ===================== */}
            <DashboardDialogs dialog={dialog}
                setDialog={setDialog}
                createTask={createTask}
                newName={newName}
                setNewName={setNewName}
                newProject={newProject}
                setNewProject={setNewProject}
                projects={projects}
                pendingTasks={pendingTasks}
                getProjectName={getProjectName}
                formatDate={formatDate} />
        </div>
    )
}
