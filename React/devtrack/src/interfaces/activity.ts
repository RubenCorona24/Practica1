import type { ReactNode } from "react"

export interface ActivityItem {
    name: string
    tone: string
    text: ReactNode
    project: string
    time: string
}