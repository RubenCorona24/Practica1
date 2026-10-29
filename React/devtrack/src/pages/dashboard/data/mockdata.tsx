import type { ActivityItem } from "@/interfaces/activity";
import type { Project, ProjectStatus } from "@/interfaces/project";
import type { Task } from "@/interfaces/task";
import { Code2, Command, Terminal } from "lucide-react";


export const projects: Project[] = [
    { id: 'devflow-web', name: 'Devflow Web', description: 'Plataforma de gestión de proyectos', status: 'active' },
    { id: 'api-gateway', name: 'API Gateway', description: 'Servicios y autenticación REST', status: 'active' },
    { id: 'design-system', name: 'Design System', description: 'Biblioteca de componentes UI', status: 'active' },
];

// Presentation details stay separate from the domain interfaces.
export const projectAppearance = [
    { projectId: 'devflow-web', tone: '', icon: Code2, initials: ['RC', 'AL', 'DM'] },
    { projectId: 'api-gateway', tone: 'blue', icon: Terminal, initials: ['RC', 'DM'] },
    { projectId: 'design-system', tone: 'amber', icon: Command, initials: ['AL', 'RC'] },
];
export const projectStatusLabels: Record<ProjectStatus, string> = { active: 'En progreso', completed: 'Completado', paused: 'Pausado' };
export const priorityLabels: Record<TaskPriority, string> = { low: 'Baja', medium: 'Media', high: 'Alta' };
export const formatDate = (date: string | null) => date ? new Intl.DateTimeFormat('es-MX', { day: 'numeric', month: 'short', timeZone: 'UTC' }).format(new Date(date)) : 'Sin fecha';

export const initialTasks: Task[] = [
    { id: 'task-1', title: 'Implementar autenticación con JWT', projectId: 'api-gateway', priority: 'high', date: '2026-10-13', status: 'in-progress' },
    { id: 'task-2', title: 'Corregir estados del componente Button', projectId: 'design-system', priority: 'medium', date: '2026-10-13', status: 'todo' },
    { id: 'task-3', title: 'Crear vista de detalle del proyecto', projectId: 'devflow-web', priority: 'high', date: '2026-10-14', status: 'in-progress' },
    { id: 'task-4', title: 'Documentar endpoints de usuarios', projectId: 'api-gateway', priority: 'low', date: null, status: 'todo' },
    { id: 'task-5', title: 'Optimizar consultas del dashboard', projectId: 'devflow-web', priority: 'medium', date: '2026-10-12', status: 'done' },
];

export const activity: ActivityItem[] = [
    { name: 'RC', tone: '', text: <><strong>Tú</strong> completaste <strong>Configurar entorno de desarrollo</strong></>, project: 'Devflow Web', time: 'Hace 15 minutos' },
    { name: 'AL', tone: 'blue', text: <><strong>Ana López</strong> comentó en <strong>Componente de navegación</strong></>, project: 'Design System', time: 'Hace 42 minutos' },
    { name: 'DM', tone: 'amber', text: <><strong>Diego Martínez</strong> creó la tarea <strong>Agregar rate limiting</strong></>, project: 'API Gateway', time: 'Hace 1 hora' },
    { name: 'RC', tone: '', text: <><strong>Tú</strong> subiste cambios a <strong>feat/project-overview</strong></>, project: 'Devflow Web', time: 'Hace 2 horas' },
    { name: 'AL', tone: 'blue', text: <><strong>Ana López</strong> completó <strong>Tokens de color y tipografía</strong></>, project: 'Design System', time: 'Hace 3 horas' },
];