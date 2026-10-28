
import { useRef, useState } from "react";
import { mockTasks, type Priority, type SortBy, type Status, type Task } from "./interfaces";
import type { Filter } from "@/c2/interface";



const statusLabel: Record<Status, string> = {
    pending: "Pendiente",
    all: "Todos",
    completed: "Completada",
    "in-progress": "En progreso"
};
const statusClass: Record<Status, string> = {
    pending: "bg-status-pending/15 text-status-pending",
    all: "bg-status-progress/15 text-status-progress",
    completed: "bg-status-done/15 text-status-done",
    "in-progress": "bg-status-pending/15 text-status-in-progress"
};
const priorityClass: Record<Priority, string> = {
    all: "bg-prio-high",
    alta: "bg-prio-high",
    media: "bg-prio-mid",
    baja: "bg-prio-low",
};
function Chip({ label, active, onClick }: { label: string; active?: boolean, onClick: () => void }) {
    return (
        <button
            onClick={onClick}
            type="button"
            className={`rounded-full border px-3 py-1.5 font-mono text-xs uppercase tracking-wider transition-colors ${active
                ? "border-foreground bg-foreground text-background"
                : "border-border bg-card text-muted-foreground hover:border-foreground hover:text-foreground"
                }`}
        >
            {label}
        </button>
    );
}

export const TaskController = () => {
    const inputRef = useRef<HTMLInputElement>(null)
    const [tasks, setTasks] = useState<Task[]>(mockTasks)
    const [search, setSearch] = useState('')
    const [statusFilter, setStatusFilter] = useState<Filter>('all')
    const [priorityFilter, setPriorityFilter] = useState<Priority>('all')
    const [sortBy, setSortBy] = useState<SortBy>('date')

    const handleSearch = (query: string) => {
        const value = query.trim().toLowerCase()
        if (!value) return;
        alert(`Buscando...${value}`)
        setSearch(value)
    }
    const handlekeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
        if (e.code !== "Enter") return;
        handleSearch(e.currentTarget.value)

    }
    const filteredTasks = tasks.filter(t => t.title.toLowerCase().includes(search.toLowerCase()))
        .filter(t => statusFilter === 'all' || t.status === statusFilter)
        .filter(t => priorityFilter === 'all' || t.priority === priorityFilter)
    console.log("Búsqueda:", search);
    console.log("Estado:", statusFilter);
    console.log("Prioridad:", priorityFilter);
    console.log("Total filtradas:", filteredTasks.length);
    console.log("Resultado:", filteredTasks);
    const sortedTasks = [...filteredTasks].sort((a, b) => {
        if (sortBy === "date") {
            return a.createdAt.getTime() - b.createdAt.getTime()
        }
        return a.title.localeCompare(b.title)
    })
    console.log("Filtro:", priorityFilter);
    console.log("Prioridades:", tasks.map(t => t.priority));
    return (
        <main className="min-h-screen bg-background px-4 py-12 sm:px-8">
            <div className="mx-auto max-w-4xl">
                <header className="mb-10 flex items-end justify-between border-b-2 border-foreground pb-4">
                    <div>
                        <p className="font-mono text-xs uppercase tracking-[0.2em] text-primary">// panel</p>
                        <h1 className="font-display text-5xl font-bold tracking-tight text-foreground">TaskController</h1>
                    </div>
                    <p className="font-mono text-sm text-muted-foreground">{filteredTasks.length} de {tasks.length} tareas</p>
                </header>

                <section className="mb-8 space-y-5 rounded-xl border border-border bg-card p-5 shadow-panel">
                    <div className="relative">
                        <span className="pointer-events-none absolute left-4 top-1/2 -translate-y-1/2 font-mono text-muted-foreground">⌕</span>
                        <input
                            onChange={(e) => setSearch(e.target.value)}
                            ref={inputRef}
                            onKeyDown={handlekeyDown}
                            placeholder="Buscar tareas por título…"
                            className="w-full rounded-lg border border-input bg-background py-3 pl-10 pr-4 text-foreground outline-none placeholder:text-muted-foreground focus:border-primary focus:ring-2 focus:ring-primary/20"
                        />
                    </div>

                    <div className="grid gap-5 sm:grid-cols-3">
                        <div>
                            <p className="mb-2 font-mono text-[11px] uppercase tracking-widest text-muted-foreground">Estado</p>
                            <div className="flex flex-wrap gap-2" >
                                <Chip label="Todas" active={statusFilter === 'all'} onClick={() => setStatusFilter('all')} />
                                <Chip label="Pendiente" active={statusFilter === 'pending'} onClick={() => setStatusFilter('pending')} />
                                <Chip label="En progreso" active={statusFilter === 'in-progress'} onClick={() => setStatusFilter('in-progress')} />
                                <Chip label="Completada" active={statusFilter === 'completed'} onClick={() => setStatusFilter('completed')} />
                            </div>
                        </div>
                        <div>
                            <p className="mb-2 font-mono text-[11px] uppercase tracking-widest text-muted-foreground">Prioridad</p>
                            <div className="flex flex-wrap gap-2">
                                <Chip label="Todas" active={priorityFilter === "all"} onClick={() => setPriorityFilter("all")} />
                                <Chip label="Alta" active={priorityFilter === "alta"} onClick={() => setPriorityFilter("alta")} />
                                <Chip label="Media" active={priorityFilter === "media"} onClick={() => setPriorityFilter("media")} />
                                <Chip label="Baja" active={priorityFilter === "baja"} onClick={() => setPriorityFilter("baja")} />
                            </div>
                        </div>
                        <div>
                            <p className="mb-2 font-mono text-[11px] uppercase tracking-widest text-muted-foreground">Ordenar por</p>
                            <div className="flex rounded-lg border border-border p-1">
                                <button
                                    className={`flex-1 rounded-md px-3 py-1.5 text-sm font-medium transition-colors ${sortBy === "date"
                                        ? "bg-primary text-primary-foreground"
                                        : "text-muted-foreground hover:text-foreground"
                                        }`}
                                    onClick={() => setSortBy("date")}
                                >
                                    Fecha ↓
                                </button>

                                <button
                                    className={`flex-1 rounded-md px-3 py-1.5 text-sm font-medium transition-colors ${sortBy === "name"
                                        ? "bg-primary text-primary-foreground"
                                        : "text-muted-foreground hover:text-foreground"
                                        }`}
                                    onClick={() => setSortBy("name")}
                                >
                                    Nombre A–Z
                                </button>
                            </div>
                        </div>
                    </div>
                </section>

                <ul className="divide-y divide-border overflow-hidden rounded-xl border border-border bg-card">
                    {sortedTasks.map((t) => (
                        <li key={t.id} className="group flex items-center gap-4 px-5 py-4 transition-colors hover:bg-muted">
                            <span className="w-8 font-mono text-xs text-muted-foreground">#{String(t.id).padStart(2, "0")}</span>
                            <span className={`h-2.5 w-2.5 shrink-0 rounded-full ${priorityClass[t.priority]}`} title={`Prioridad ${t.priority}`} />
                            <span className={`flex-1 font-medium text-foreground ${t.status === "completed" ? "line-through opacity-60" : ""}`}>
                                {t.title}
                            </span>
                            <span className="hidden font-mono text-xs uppercase text-muted-foreground sm:inline">{t.priority}</span>
                            <span className={`rounded-full px-2.5 py-1 font-mono text-[11px] uppercase tracking-wider ${statusClass[t.status]}`}>
                                {statusLabel[t.status]}
                            </span>
                            <time className="w-24 text-right font-mono text-xs text-muted-foreground">
                                {t.createdAt.toLocaleDateString("es-MX", { day: "2-digit", month: "short", year: "numeric" })}
                            </time>
                        </li>
                    ))}
                </ul>
            </div>
        </main>
    );
}