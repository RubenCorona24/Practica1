
export type ProjectStatus = 'active' | 'completed' | 'paused'

export interface Project {
    id: string
    name: string
    description: string
    status: ProjectStatus

}