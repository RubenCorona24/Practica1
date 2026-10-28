// ¿Qué campos necesita una tarea?
// ¿Qué tipos necesitas para los filtros?
export type Status = 'all' | 'pending' | 'completed' | "in-progress"
export type Priority = 'all' | 'alta' | 'media' | 'baja'
export type SortBy = 'name' | 'date'

export interface Task {
    id: number
    title: string
    status: Status       // ← ¿qué valores puede tener?
    priority: Priority     // ← ¿qué valores puede tener?
    createdAt: Date   // ← para ordenar por fecha
}
export const mockTasks: Task[] = [
    { id: 1, title: "Diseñar UI", status: "completed", priority: "alta", createdAt: new Date("2024-01-15") },
    { id: 2, title: "Implementar API", status: "in-progress", priority: "alta", createdAt: new Date("2024-02-20") },
    { id: 3, title: "Escribir tests", status: "pending", priority: "media", createdAt: new Date("2024-03-10") },
    { id: 4, title: "Deploy", status: "pending", priority: "baja", createdAt: new Date("2024-04-05") },
    { id: 5, title: "Documentación", status: "in-progress", priority: "media", createdAt: new Date("2024-01-30") },
]

