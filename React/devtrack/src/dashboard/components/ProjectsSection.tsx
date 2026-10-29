
import { Button } from "@/components/ui/button";
import type { Project } from "@/interfaces/project";
import { X } from "lucide-react";

interface Props {
    selectedProject: Project | undefined,
    visibleProjects: Project[],
    project: string,
    onSetProject: (id: string) => void
}
export const ProjectsSection = ({ project, selectedProject, visibleProjects, onSetProject }: Props) => {
    return (
        <div className="section-title">
            <h2>
                {selectedProject?.name || 'Proyectos'}
                <span className="count">{visibleProjects.length}</span>
            </h2>
            {project ? (
                <Button variant="ghost" size="sm" onClick={() => onSetProject('')}>
                    Todos los proyectos <X />
                </Button>
            ) : (
                <span className="text-[11px] text-muted-foreground">Tu trabajo en curso</span>
            )}
        </div>
    )
}
