
//Definimos tipos de Task por estatus y prioridad
export type TaskStatus = 'todo' | 'in-progress' | 'done'
export type TaskPriority = 'low' | 'medium' | 'high'

//Interfaz de cada tarea
export interface Task {
    id: string
    projectId: string
    title: string
    status: TaskStatus
    priority: TaskPriority
    date: string | null
}