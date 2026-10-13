import type { Project } from "@/interfaces/project";
import type { Task } from "@/interfaces/task";
import { Code2, Command, Terminal, type LucideIcon } from "lucide-react";

export const projects: Project[] = [
    { id: '1', name: 'Devflow Web', description: 'Plataforma de gestión de proyectos', status: 'active' },
    { id: '2', name: 'API Gateway', description: 'Servicios y autenticación REST', status: 'active' },
    { id: '3', name: 'Design System', description: 'Biblioteca de componentes UI', status: 'active' },
];

export const projectUI: Record<string, { tone: string; icon: LucideIcon }> = {
    '1': { tone: '', icon: Code2 },
    '2': { tone: 'blue', icon: Terminal },
    '3': { tone: 'amber', icon: Command },
};

export const initialTasks: Task[] = [
    { id: '1', title: 'Implementar autenticación con JWT', projectId: '1', priority: 'high', date: 'Hoy', status: 'todo' },
    { id: '2', title: 'Corregir estados del componente Button', projectId: '2', priority: 'medium', date: 'Hoy', status: 'todo' },
    { id: '3', title: 'Crear vista de detalle del proyecto', projectId: '3', priority: 'high', date: '12 oct', status: 'todo' },
    { id: '4', title: 'Documentar endpoints de usuarios', projectId: '4', priority: 'low', date: '13 oct', status: 'todo' },
    { id: '5', title: 'Optimizar consultas del dashboard', projectId: '5', priority: 'medium', date: '14 oct', status: 'todo' },
];

export const activity = [
    { name: 'RC', tone: '', text: <><strong>Tú</strong> completaste <strong>Configurar entorno de desarrollo</strong></>, project: 'Devflow Web', time: 'Hace 15 minutos' },
    { name: 'AL', tone: 'blue', text: <><strong>Ana López</strong> comentó en <strong>Componente de navegación</strong></>, project: 'Design System', time: 'Hace 42 minutos' },
    { name: 'DM', tone: 'amber', text: <><strong>Diego Martínez</strong> creó la tarea <strong>Agregar rate limiting</strong></>, project: 'API Gateway', time: 'Hace 1 hora' },
    { name: 'RC', tone: '', text: <><strong>Tú</strong> subiste cambios a <strong>feat/project-overview</strong></>, project: 'Devflow Web', time: 'Hace 2 horas' },
    { name: 'AL', tone: 'blue', text: <><strong>Ana López</strong> completó <strong>Tokens de color y tipografía</strong></>, project: 'Design System', time: 'Hace 3 horas' },
];