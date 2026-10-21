import { useState, type FormEvent } from 'react'
import {
    Activity, Check, CheckCheck, ChevronRight,
    Code2, FolderKanban, GitBranch, Plus, X,
} from 'lucide-react'
import { Button } from '@/components/ui/button'
import { Dialog, DialogContent, DialogHeader, DialogTitle } from '@/components/ui/dialog'
import {
    activity,
    formatDate,
    initialTasks,
    priorityLabels,
    projectAppearance,
    projects,
    projectStatusLabels,
} from './data/mockdata'
import { SidebarComponent } from '@/dashboard/components/Sidebar'
import { Topbar } from '@/dashboard/components/Topbar'
import { PageHeading } from '@/dashboard/components/PageHeading'
import { StatsGrid } from '@/dashboard/components/StatsGrid'
import { ProjectCard } from '@/dashboard/components/ProjectCard'
import { ProjectsSection } from '@/dashboard/components/ProjectsSection'

/* -------------------------------------------------------------------------- */
/*  Constantes de presentación                                                */
/* -------------------------------------------------------------------------- */

const WEEKDAYS = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
const CHART_GRID_Y = [15, 50, 85, 120]


const PRIORITY_TONE: Record<string, string> = { high: 'rose', medium: 'amber', low: 'blue' }
const PRIORITY_ARROW: Record<string, string> = { high: '↑', medium: '−', low: '↓' }

const DIALOG_TITLES = {
    task: 'Nueva tarea',
    notifications: 'Notificaciones',
    help: 'Centro de ayuda',
}

const CHART_THIS_WEEK = {
    line: 'M25 85 C60 85 75 106 112 103 S160 35 200 50 S240 90 288 68 S325 10 376 32 S430 76 464 63 S510 28 550 38',
    fill: 'M25 85 C60 85 75 106 112 103 S160 35 200 50 S240 90 288 68 S325 10 376 32 S430 76 464 63 S510 28 550 38 L550 120 L25 120Z',
}
const CHART_LAST_WEEK = {
    line: 'M25 105 Q100 55 112 80 T200 100 T288 80 T376 50 T464 90 T550 80',
    fill: 'M25 105 Q100 55 112 80 T200 100 T288 80 T376 50 T464 90 T550 80 L550 120 L25 120Z',
}

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
    const [period, setPeriod] = useState('Esta semana')
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

    const isThisWeek = period === 'Esta semana'
    const chartPaths = isThisWeek ? CHART_THIS_WEEK : CHART_LAST_WEEK

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
    const clearSelection = () => {
        setProject('')
        setSearch('')
    }

    const toggleProject = (id: string) => setProject(project === id ? '' : id)

    const toggleTask = (id: string) =>
        setTasks(
            tasks.map(item =>
                item.id === id
                    ? { ...item, status: item.status === 'done' ? 'todo' : 'done' }
                    : item,
            ),
        )

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
                            <div className="section-title">
                                <h2>Mis tareas<span className="count">{visibleTasks.length}</span></h2>
                                <select
                                    aria-label="Filtrar tareas"
                                    className="text-[11px] bg-transparent text-muted-foreground outline-none"
                                    value={filter}
                                    onChange={e => setFilter(e.target.value)}
                                >
                                    <option>Todas</option>
                                    <option>Pendientes</option>
                                    <option>Completadas</option>
                                </select>
                            </div>

                            <div className="task-table">
                                {visibleTasks.map(t => {
                                    const isDone = t.status === 'done'
                                    return (
                                        <div className={`task-row ${isDone ? 'done' : ''}`} key={t.id}>
                                            <input
                                                type="checkbox"
                                                className="task-check"
                                                checked={isDone}
                                                aria-label={`Completar ${t.title}`}
                                                onChange={() => toggleTask(t.id)}
                                            />
                                            <div>
                                                <div className="task-name">{t.title}</div>
                                                <div className="task-project">{getProjectName(t.projectId)}</div>
                                            </div>
                                            <span className={`badge ${PRIORITY_TONE[t.priority]}`}>
                                                {PRIORITY_ARROW[t.priority]} {priorityLabels[t.priority]}
                                            </span>
                                            <span className="task-date text-[10px] text-muted-foreground">
                                                {formatDate(t.date)}
                                            </span>
                                        </div>
                                    )
                                })}
                                {!visibleTasks.length && (
                                    <p className="subtext p-6 text-center">No hay tareas en esta vista.</p>
                                )}
                            </div>

                            {/* ===================== Productividad ===================== */}
                            <div className="activity-chart">
                                <div className="section-title">
                                    <h2>Tu productividad</h2>
                                    <select
                                        aria-label="Periodo de productividad"
                                        className="text-[11px] bg-transparent text-muted-foreground outline-none"
                                        value={period}
                                        onChange={e => setPeriod(e.target.value)}
                                    >
                                        <option>Esta semana</option>
                                        <option>Semana anterior</option>
                                    </select>
                                </div>

                                <div className="flex gap-4 items-center mb-3">
                                    <span className="text-[11px] text-muted-foreground flex items-center gap-1.5">
                                        <span className="status-dot" />Tareas completadas
                                    </span>
                                    <span className="text-[11px] positive">
                                        {isThisWeek ? 12 + completed : 9} en total
                                    </span>
                                </div>

                                <svg
                                    className="chart"
                                    viewBox="0 0 560 145"
                                    role="img"
                                    aria-label={`Gráfica de tareas completadas: ${period}`}
                                    preserveAspectRatio="none"
                                >
                                    {CHART_GRID_Y.map((y, i) => (
                                        <g key={y}>
                                            <text x="0" y={y + 3} className="chart-label">{6 - i * 2}</text>
                                            <line x1="25" x2="550" y1={y} y2={y} className="chart-grid" />
                                        </g>
                                    ))}
                                    <path className="chart-fill" d={chartPaths.fill} />
                                    <path className="chart-line" d={chartPaths.line} />
                                    {WEEKDAYS.map((d, i) => (
                                        <text
                                            className="chart-label"
                                            key={d}
                                            x={25 + i * 87}
                                            y="142"
                                            textAnchor={i === 6 ? 'end' : 'start'}
                                        >
                                            {d}
                                        </text>
                                    ))}
                                </svg>
                            </div>
                        </section>

                        {/* ===================== Actividad reciente ===================== */}
                        <section>
                            <div className="section-title">
                                <h2>Actividad reciente</h2>
                                <Activity size={16} className="text-muted-foreground" />
                            </div>
                            <div className="activity-list">
                                {visibleActivity.map((a, i) => (
                                    <div className="activity-item" key={i}>
                                        <span className={`avatar ${a.tone}`}>{a.name}</span>
                                        <div>
                                            <p>{a.text}</p>
                                            <div className="task-project">{a.project}</div>
                                            <time>{a.time}</time>
                                        </div>
                                    </div>
                                ))}
                            </div>
                        </section>
                    </div>

                    <footer className="footer">
                        <span>Un paso a la vez. Cada commit cuenta.</span>
                        <span><span className="status-dot" />Vista de ejemplo</span>
                    </footer>
                </main>
            </div>

            {/* ===================== Diálogo ===================== */}
            <Dialog open={dialog !== null} onOpenChange={open => { if (!open) setDialog(null) }}>
                <DialogContent>
                    <DialogHeader>
                        <DialogTitle>{dialog ? DIALOG_TITLES[dialog] : ''}</DialogTitle>
                    </DialogHeader>

                    {dialog === 'task' && (
                        <form className="space-y-4" onSubmit={createTask}>
                            <label className="block text-sm">
                                Nombre de la tarea
                                <input
                                    autoFocus
                                    required
                                    className="mt-2 w-full rounded-md border border-input bg-background p-3 outline-none focus:border-primary"
                                    placeholder="¿En qué vas a trabajar?"
                                    value={newName}
                                    onChange={e => setNewName(e.target.value)}
                                />
                            </label>

                            <label className="block text-sm">
                                Proyecto
                                <select
                                    className="mt-2 w-full rounded-md border border-input bg-background p-3"
                                    value={newProject}
                                    onChange={e => setNewProject(e.target.value)}
                                >
                                    {projects.map(p => (
                                        <option key={p.id} value={p.id}>{p.name}</option>
                                    ))}
                                </select>
                            </label>

                            <div className="flex justify-end">
                                <Button type="submit"><Plus />Crear tarea</Button>
                            </div>
                        </form>
                    )}

                    {dialog === 'notifications' && (
                        <div className="space-y-4 py-3">
                            <p className="text-sm font-medium">Tareas pendientes con fecha</p>
                            {pendingTasks.filter(t => t.date).map(t => (
                                <p key={t.id} className="subtext">
                                    {t.title} · {getProjectName(t.projectId)} · {formatDate(t.date)}
                                </p>
                            ))}
                            {!pendingTasks.some(t => t.date) && (
                                <p className="subtext">No hay tareas pendientes con fecha.</p>
                            )}
                        </div>
                    )}

                    {dialog === 'help' && (
                        <p className="subtext py-3">
                            Esta es una vista de ejemplo. Puedes buscar proyectos y tareas, marcar tareas
                            como completadas o crear una nueva. Los cambios duran mientras mantengas abierta
                            la página.
                        </p>
                    )}
                </DialogContent>
            </Dialog>
        </div>
    )
}
