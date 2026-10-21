import type { Task } from "@/interfaces/task"

interface Props {
    tasks: Task[]
    filter: string
    onSetFilter: (e: React.ChangeEvent<HTMLSelectElement, HTMLSelectElement>) => void
}
export const TasksSection = ({ tasks, filter, onSetFilter }: Props) => {
    return (
        <div className="section-title">
            <h2>Mis tareas<span className="count">{tasks.length}</span></h2>
            <select
                aria-label="Filtrar tareas"
                className="text-[11px] bg-transparent text-muted-foreground outline-none"
                value={filter}
                onChange={onSetFilter}
            >
                <option>Todas</option>
                <option>Pendientes</option>
                <option>Completadas</option>
            </select>
        </div>
    )
}
