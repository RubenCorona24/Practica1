import type { Task } from "@/interfaces/task"

type TaskFilter = "Todas" | "Pendientes" | "Completadas"
interface Props {
    tasks: Task[]
    filter: string
    onSetFilter: (filter: TaskFilter) => void
}
export const TasksSection = ({ tasks, filter, onSetFilter }: Props) => {
    return (
        <div className="section-title">
            <h2>Mis tareas<span className="count">{tasks.length}</span></h2>
            <select
                aria-label="Filtrar tareas"
                className="text-[11px] bg-transparent text-muted-foreground outline-none"
                value={filter}
                onChange={(e) => onSetFilter(e.target.value as TaskFilter)}
            >
                <option>Todas</option>
                <option>Pendientes</option>
                <option>Completadas</option>
            </select>
        </div>
    )
}
