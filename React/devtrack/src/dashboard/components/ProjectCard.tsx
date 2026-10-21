
import { Button } from "@/components/ui/button";
import type { Project } from "@/interfaces/project";
import { formatDate, projectStatusLabels } from "@/pages/dashboard/data/mockdata";
import { GitBranch, Icon } from "lucide-react";

const AVATAR_TONES = ['', 'blue', 'amber']
interface Props {
    project: Project
    onSetProject: (id: string) => void;
}
export const ProjectCard = ({ project, onSetProject }: Props) => {
    return (

        <article className="project-card" key={project.id}>
            <div className="flex justify-between items-center">
                <span className={`project-icon ${project.tone}`}><Icon size={22} /></span>
                <span className={`badge ${project.tone}`}>{projectStatusLabels[project.status]}</span>
            </div>

            <h3>
                <Button
                    variant="link"
                    className="p-0 h-auto text-foreground text-sm"
                    onClick={() => onSetProject(project.id)}
                >
                    {project.name}
                </Button>
            </h3>
            <p className="subtext text-xs">{project.description}</p>

            <div className="flex justify-between text-[10px] mt-5">
                <span className="text-muted-foreground">{project.completed} de {project.total} tareas</span>
                <span className="font-semibold">{project.progress}%</span>
            </div>
            <div className={`progress-track ${project.tone}`}>
                <progress max={100} value={project.progress} aria-label={`Progreso de ${project.name}`} />
            </div>

            <div className="flex justify-between items-center">
                <div className="flex -space-x-2">
                    {project.initials.map((n, i) => (
                        <span key={n} className={`avatar ${AVATAR_TONES[i]}`}>{n}</span>
                    ))}
                </div>
                <span className="text-[10px] text-muted-foreground flex items-center gap-1.5">
                    <GitBranch size={12} />
                    {project.nextDate ? `Próxima tarea ${formatDate(project.nextDate)}` : 'Sin fecha pendiente'}
                </span>
            </div>
        </article>
    )
}
