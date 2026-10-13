
import { useState } from 'react';
import { Activity, ArrowUpRight, Bell, Check, CheckCheck, ChevronDown, ChevronRight, CircleHelp, Code2, Command, FolderKanban, GitBranch, LayoutDashboard, Plus, Search, Terminal, X, type LucideIcon } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Dialog, DialogContent, DialogHeader, DialogTitle } from '@/components/ui/dialog';
import type { Task } from '@/interfaces/task';
import { activity, initialTasks, projects, projectUI } from './data/mockdata';


const priorityLabel = { high: 'Alta', medium: 'Media', low: 'Baja' } as const
const today = new Date().toLocaleDateString('en-CA') // YYYY-MM-DD en hora local
const formatDue = (d: string | null) =>
    !d ? 'Sin fecha'
        : d === today ? 'Hoy'
            : new Date(d + 'T00:00:00').toLocaleDateString('es-MX', { day: 'numeric', month: 'short' })
const projectName = (id: string) => projects.find(p => p.id === id)?.name ?? ''
export function Dashboard() {

    const [tasks, setTasks] = useState(initialTasks);
    const [search, setSearch] = useState('');
    const [project, setProject] = useState('');
    const [filter, setFilter] = useState('Todas');
    const [dialog, setDialog] = useState<'task' | 'notifications' | 'help' | null>(null);
    const [newName, setNewName] = useState('');
    const [newProject, setNewProject] = useState('Devflow Web');
    const [period, setPeriod] = useState('Esta semana');

    const completed = tasks.filter(t => t.status === 'done').length;
    const q = search.toLowerCase()

    const visibleTasks = tasks.filter(t =>
        (!project || t.projectId === project) &&
        (filter !== 'Pendientes' || t.status !== 'done') &&
        (filter !== 'Completadas' || t.status === 'done') &&
        `${t.title} ${projectName(t.projectId)}`.toLowerCase().includes(q));
    const visibleProjects = projects.filter(p =>
        (!project || p.id === project) &&
        (!q || `${p.name} ${p.description}`.toLowerCase().includes(q) ||
            tasks.some(t => t.projectId === p.id && t.title.toLowerCase().includes(q))));
    const projectStats = (id: string) => {
        const list = tasks.filter(t => t.projectId === id)
        const done = list.filter(t => t.status === 'done').length
        return { total: list.length, completed: done, progress: list.length ? Math.round((done / list.length) * 100) : 0 }
    }
    return (
        <div className="app-layout">
            <aside className="sidebar">
                <div className="brand"><span className="brand-mark"><Code2 size={22} /></span>devflow<span className="text-primary">.</span></div>
                <div className="workspace"><span className="workspace-icon">D</span><div className="flex-1"><strong>Dev workspace</strong><div className="text-muted-foreground text-[10px] mt-1">Espacio personal</div></div><ChevronDown size={14} /></div>
                <div className="nav-label">Workspace</div>
                <Button variant="ghost" className={`nav-button ${!project ? 'active' : ''}`} onClick={() => { setProject(''); setSearch(''); }}><LayoutDashboard />Dashboard</Button>
                <div className="nav-label">Tus proyectos <span className="float-right">3</span></div>
                {projects.map(p => <Button key={p.id} variant="ghost" className={`nav-button ${project === p.id ? 'active' : ''}`} onClick={() => setProject(project === p.id ? '' : p.id)}><span className={`project-dot ${projectUI[p.id].tone}`} />{p.id}</Button>)}
                <div className="sidebar-bottom">
                    <Button variant="ghost" className="nav-button text-muted-foreground" onClick={() => setDialog('help')}><CircleHelp />Centro de ayuda<ArrowUpRight className="ml-auto" /></Button>
                    <div className="flex items-center gap-3 mt-4"><span className="avatar">RC</span><div><div className="text-xs font-semibold">Rubén Corona</div><div className="text-[10px] text-muted-foreground mt-1">Desarrollador</div></div></div>
                </div>
            </aside>

            <div className="main-column">
                <header className="topbar">
                    <div className="search"><Search size={17} /><input aria-label="Buscar proyectos y tareas" placeholder="Buscar proyectos, tareas..." value={search} onChange={e => setSearch(e.target.value)} />{search && <Button variant="ghost" size="icon" title="Limpiar búsqueda" onClick={() => setSearch('')}><X /></Button>}</div>
                    <div className="flex items-center gap-4"><Button variant="ghost" size="icon" title="Notificaciones" onClick={() => setDialog('notifications')}><Bell /></Button><span className="h-6 border-l border-border" /><span className="avatar">RC</span></div>
                </header>

                <main className="content">
                    <div className="page-heading"><div><div className="flex items-center gap-2 text-[11px] text-muted-foreground mb-3"><span>Workspace</span><ChevronRight size={12} /><span className="text-foreground">Dashboard</span></div><h1>Buen día, Rubén <span className="text-xl">✦</span></h1><p className="subtext mt-1">Vamos a construir algo increíble hoy.</p></div><Button className="mt-8" onClick={() => setDialog('task')}><Plus />Nueva tarea</Button></div>

                    <div className="stats">
                        {[{ label: 'Proyectos activos', value: '3', icon: FolderKanban, tone: '', note: 'Todos en marcha', change: '+1' },
                        { label: 'Tareas pendientes', value: String(18 - completed + tasks.length - initialTasks.length), icon: CheckCheck, tone: 'blue', note: 'asignadas a ti', change: '5 para hoy' },
                        { label: 'Completadas esta semana', value: String(12 + completed), icon: Check, tone: '', note: 'vs. semana anterior', change: '+33%' },
                        { label: 'Próximas entregas', value: '2', icon: GitBranch, tone: 'amber', note: 'en los próximos 7 días', change: 'Esta semana' }].map(s => <div className="stat" key={s.label}><div className="stat-top"><span>{s.label}</span><span className={`stat-icon ${s.tone}`}><s.icon size={17} /></span></div><div className="stat-value">{s.value}</div><div className="stat-note"><span className={s.tone === 'amber' ? 'warning' : 'positive'}>{s.change}</span> <span>{s.note}</span></div></div>)}
                    </div>

                    <section>
                        <div className="section-title"><h2>{project || 'Proyectos activos'}<span className="count">{visibleProjects.length}</span></h2>{project ? <Button variant="ghost" size="sm" onClick={() => setProject('')}>Todos los proyectos <X /></Button> : <span className="text-[11px] text-muted-foreground">Tu trabajo en curso</span>}</div>
                        <div className="project-grid">
                            {visibleProjects.map(p => {
                                const ui = projectUI[p.id]
                                const Icon = ui.icon
                                const { total, completed, progress } = projectStats(p.id)
                                return (
                                    <article className="project-card" key={p.id}>
                                        <div className="flex justify-between items-center">
                                            <span className={`project-icon ${ui.tone}`}><Icon size={22} /></span>
                                            <span className={`badge ${ui.tone}`}>{p.status}</span>
                                        </div>
                                        <h3><Button variant="link" className="p-0 h-auto text-foreground text-sm" onClick={() => setProject(p.id)}>{p.name}</Button></h3>
                                        <p className="subtext text-xs">{p.description}</p>
                                        <div className="flex justify-between text-[10px] mt-5">
                                            <span className="text-muted-foreground">{completed} de {total} tareas</span>
                                            <span className="font-semibold">{progress}%</span>
                                        </div>
                                        <div className={`progress-track ${ui.tone}`}>
                                            <progress max={100} value={progress} aria-label={`Progreso de ${p.name}`} />
                                        </div>
                                    </article>
                                )
                            })}
                        </div>
                        {!visibleProjects.length && <p className="subtext mb-6">No se encontraron proyectos.</p>}
                    </section>

                    <div className="lower-grid">
                        <section>
                            <div className="section-title"><h2>Mis tareas<span className="count">{visibleTasks.length}</span></h2><select aria-label="Filtrar tareas" className="text-[11px] bg-transparent text-muted-foreground outline-none" value={filter} onChange={e => setFilter(e.target.value)}><option>Todas</option><option>Pendientes</option><option>Completadas</option></select></div>
                            <div className="task-table">
                                {visibleTasks.map(t => {
                                    const done = t.status === 'done'
                                    return (
                                        <div className={`task-row ${done ? 'done' : ''}`} key={t.id}>
                                            <input type="checkbox" className="task-check" checked={done} aria-label={`Completar ${t.title}`}
                                                onChange={() => setTasks(tasks.map((item): Task =>
                                                    item.id === t.id ? { ...item, status: done ? 'todo' : 'done' } : item))} />
                                            <div>
                                                <div className="task-name">{t.title}</div>
                                                <div className="task-project">{projectName(t.projectId)}</div>
                                            </div>
                                            <span className={`badge ${t.priority === 'high' ? 'rose' : t.priority === 'medium' ? 'amber' : 'blue'}`}>
                                                {t.priority === 'high' ? '↑' : t.priority === 'medium' ? '−' : '↓'} {priorityLabel[t.priority]}
                                            </span>
                                            <span className={`task-date text-[10px] ${t.date === today ? 'warning' : 'text-muted-foreground'}`}>
                                                {formatDue(t.date)}
                                            </span>
                                        </div>
                                    )
                                })}
                                {!visibleTasks.length && <p className="subtext p-6 text-center">No hay tareas en esta vista.</p>}
                            </div>
                            <div className="activity-chart">
                                <div className="section-title"><h2>Tu productividad</h2><select aria-label="Periodo de productividad" className="text-[11px] bg-transparent text-muted-foreground outline-none" value={period} onChange={e => setPeriod(e.target.value)}><option>Esta semana</option><option>Semana anterior</option></select></div>
                                <div className="flex gap-4 items-center mb-3"><span className="text-[11px] text-muted-foreground flex items-center gap-1.5"><span className="status-dot" />Tareas completadas</span><span className="text-[11px] positive">{period === 'Esta semana' ? 12 + completed : 9} en total</span></div>
                                <svg className="chart" viewBox="0 0 560 145" role="img" aria-label={`Gráfica de tareas completadas: ${period}`} preserveAspectRatio="none">
                                    {[15, 50, 85, 120].map((y, i) => <g key={y}><text x="0" y={y + 3} className="chart-label">{6 - i * 2}</text><line x1="25" x2="550" y1={y} y2={y} className="chart-grid" /></g>)}
                                    <path className="chart-fill" d={period === 'Esta semana' ? 'M25 85 C60 85 75 106 112 103 S160 35 200 50 S240 90 288 68 S325 10 376 32 S430 76 464 63 S510 28 550 38 L550 120 L25 120Z' : 'M25 105 Q100 55 112 80 T200 100 T288 80 T376 50 T464 90 T550 80 L550 120 L25 120Z'} />
                                    <path className="chart-line" d={period === 'Esta semana' ? 'M25 85 C60 85 75 106 112 103 S160 35 200 50 S240 90 288 68 S325 10 376 32 S430 76 464 63 S510 28 550 38' : 'M25 105 Q100 55 112 80 T200 100 T288 80 T376 50 T464 90 T550 80'} />
                                    {['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom'].map((d, i) => <text className="chart-label" key={d} x={25 + i * 87} y="142" textAnchor={i === 6 ? 'end' : 'start'}>{d}</text>)}
                                </svg>
                            </div>
                        </section>

                        <section>
                            <div className="section-title"><h2>Actividad reciente</h2><Activity size={16} className="text-muted-foreground" /></div>
                            <div className="activity-list">
                                {activity.filter(a => !project || a.project === project).map((a, i) => <div className="activity-item" key={i}><span className={`avatar ${a.tone}`}>{a.name}</span><div><p>{a.text}</p><div className="task-project">{a.project}</div><time>{a.time}</time></div></div>)}
                            </div>
                        </section>
                    </div>

                    <footer className="footer"><span>Un paso a la vez. Cada commit cuenta.</span><span><span className="status-dot" />Vista de ejemplo</span></footer>
                </main>
            </div>

            <Dialog open={dialog !== null} onOpenChange={open => { if (!open) setDialog(null); }}>
                <DialogContent>
                    <DialogHeader><DialogTitle>{dialog === 'task' ? 'Nueva tarea' : dialog === 'notifications' ? 'Notificaciones' : 'Centro de ayuda'}</DialogTitle></DialogHeader>
                    {dialog === 'task' ? <form className="space-y-4" onSubmit={e => {
                        e.preventDefault()
                        if (!newName.trim()) return
                        setTasks([...tasks, {
                            id: crypto.randomUUID(), projectId: newProject, title: newName.trim(),
                            status: 'todo', priority: 'medium', date: today,
                        }])
                        setNewName(''); setDialog(null)
                    }}><label className="block text-sm">Nombre de la tarea<input autoFocus required className="mt-2 w-full rounded-md border border-input bg-background p-3 outline-none focus:border-primary" placeholder="¿En qué vas a trabajar?" value={newName} onChange={e => setNewName(e.target.value)} /></label><label className="block text-sm">Proyecto<select className="mt-2 w-full rounded-md border border-input bg-background p-3" value={newProject} onChange={e => setNewProject(e.target.value)}>{projects.map(p => <option key={p.name}>{p.name}</option>)}</select></label><div className="flex justify-end"><Button type="submit"><Plus />Crear tarea</Button></div></form> : dialog === 'notifications' ? <div className="space-y-4 py-3"><p className="text-sm font-medium">2 próximas entregas</p><p className="subtext">Design System · 15 de octubre</p><p className="subtext">Devflow Web · 18 de octubre</p></div> : <p className="subtext py-3">Esta es una vista de ejemplo. Puedes buscar proyectos y tareas, marcar tareas como completadas o crear una nueva. Los cambios duran mientras mantengas abierta la página.</p>}
                </DialogContent>
            </Dialog>
        </div>
    );
}
