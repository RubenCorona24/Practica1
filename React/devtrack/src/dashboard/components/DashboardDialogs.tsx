import { Dialog, DialogContent, DialogHeader, DialogTitle } from '@/components/ui/dialog'

import { Button } from '@/components/ui/button'
import { Plus } from 'lucide-react'
import type { FormEvent } from 'react'
import type { Project } from '@/interfaces/project'
import type { Task } from '@/interfaces/task'

interface Props {
    //Values
    dialog: "task" | "notifications" | "help" | null
    projects: Project[]
    pendingTasks: Task[]
    newProject: string
    newName: string
    //Functions
    getProjectName: (id: string) => string
    setDialog: (value: React.SetStateAction<"task" | "notifications" | "help" | null>) => void
    createTask: (e: FormEvent<HTMLFormElement>) => void;
    setNewName: (name: string) => void;
    setNewProject: (projectName: string) => void;

    formatDate: (date: string | null) => string;


}
const DIALOG_TITLES = {
    task: 'Nueva tarea',
    notifications: 'Notificaciones',
    help: 'Centro de ayuda',
}
export const DashboardDialogs = ({ dialog, projects, pendingTasks, newProject, newName, getProjectName,
    setDialog, createTask, setNewName, setNewProject, formatDate
}: Props) => {

    return (
        <Dialog open={dialog !== null} onOpenChange={open => { if (!open) setDialog(null) }}>
            <DialogContent>
                <DialogHeader>
                    <DialogTitle>{dialog ? DIALOG_TITLES[dialog] : ''}</DialogTitle>
                </DialogHeader>

                {dialog === 'task' && (
                    <form className="space-y-4" onSubmit={createTask}>
                        <label className="block text-sm">
                            Nombre de la tarea
                            <input
                                autoFocus
                                required
                                className="mt-2 w-full rounded-md border border-input bg-background p-3 outline-none focus:border-primary"
                                placeholder="¿En qué vas a trabajar?"
                                value={newName}
                                onChange={e => setNewName(e.target.value)}
                            />
                        </label>

                        <label className="block text-sm">
                            Proyecto
                            <select
                                className="mt-2 w-full rounded-md border border-input bg-background p-3"
                                value={newProject}
                                onChange={e => setNewProject(e.target.value)}
                            >
                                {projects.map(p => (
                                    <option key={p.id} value={p.id}>{p.name}</option>
                                ))}
                            </select>
                        </label>

                        <div className="flex justify-end">
                            <Button type="submit"><Plus />Crear tarea</Button>
                        </div>
                    </form>
                )}

                {dialog === 'notifications' && (
                    <div className="space-y-4 py-3">
                        <p className="text-sm font-medium">Tareas pendientes con fecha</p>
                        {pendingTasks.filter(t => t.date).map(t => (
                            <p key={t.id} className="subtext">
                                {t.title} · {getProjectName(t.projectId)} · {formatDate(t.date)}
                            </p>
                        ))}
                        {!pendingTasks.some(t => t.date) && (
                            <p className="subtext">No hay tareas pendientes con fecha.</p>
                        )}
                    </div>
                )}

                {dialog === 'help' && (
                    <p className="subtext py-3">
                        Esta es una vista de ejemplo. Puedes buscar proyectos y tareas, marcar tareas
                        como completadas o crear una nueva. Los cambios duran mientras mantengas abierta
                        la página.
                    </p>
                )}
            </DialogContent>
        </Dialog>
    )
}
