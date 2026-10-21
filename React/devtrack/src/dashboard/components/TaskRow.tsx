import type { Task } from "@/interfaces/task"
import { formatDate, priorityLabels } from "@/pages/dashboard/data/mockdata"

interface TaskRowProps {
    task: Task
    projectName: string
    onToggle: (taskId: string) => void
}
const PRIORITY_ARROW: Record<string, string> = { high: '↑', medium: '−', low: '↓' }
const PRIORITY_TONE: Record<string, string> = { high: 'rose', medium: 'amber', low: 'blue' }

export const TaskRow = ({ task, projectName, onToggle }: TaskRowProps) => {
    const isDone = task.status === 'done'
    return (
        <div className={`task-row ${isDone ? 'done' : ''}`} >
            <input
                type="checkbox"
                className="task-check"
                checked={isDone}
                aria-label={`Completar ${task.title}`}
                onChange={() => onToggle(task.id)}
            />
            <div>
                <div className="task-name">{task.title}</div>
                <div className="task-project">{projectName}</div>
            </div>
            <span className={`badge ${PRIORITY_TONE[task.priority]}`}>
                {PRIORITY_ARROW[task.priority]} {priorityLabels[task.priority]}
            </span>
            <span className="task-date text-[10px] text-muted-foreground">
                {formatDate(task.date)}
            </span>
        </div>
    )
}
