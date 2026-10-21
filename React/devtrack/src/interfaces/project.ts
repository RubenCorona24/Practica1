import type { LucideIcon } from "lucide-react"

export type ProjectStatus = 'active' | 'completed' | 'paused'

export interface Project {
    id: string
    name: string
    description: string
    status: 'active' | 'completed' | 'paused'
    tone: string
    icon: LucideIcon
    completed: number
    total: number
    progress: number
    initials: string[]
    nextDate: string | null
}