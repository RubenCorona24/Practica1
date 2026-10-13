import { Button } from "@/components/ui/button";
import type { Project } from "@/interfaces/project";
import { ArrowUpRight, ChevronDown, CircleHelp, Code2, LayoutDashboard } from "lucide-react";

interface Props {
    projects: Project[],
    project: string;
    onProjectChange: (project: string) => void
    onSearchReset: () => void;
    onOpenHelp: () => void;
}
export const Sidebar = ({ projects, project, onProjectChange, onSearchReset, onOpenHelp }: Props) => {
    const handleDashboardClick = () => {
        onProjectChange("")
        onSearchReset()
    }
    const handleProjectClcik = (name: string) => {
        onProjectChange(project === name ? '' : name)
    }
    return (
        <div>
            <aside className="sidebar">
                <div className="brand"><span className="brand-mark"><Code2 size={22} /></span>devflow<span className="text-primary">.</span></div>
                <div className="workspace"><span className="workspace-icon">D</span><div className="flex-1"><strong>Dev workspace</strong><div className="text-muted-foreground text-[10px] mt-1">Espacio personal</div></div><ChevronDown size={14} /></div>
                <div className="nav-label">Workspace</div>
                <Button variant="ghost" className={`nav-button ${!project ? 'active' : ''}`} onClick={handleDashboardClick}><LayoutDashboard />Dashboard</Button>
                <div className="nav-label">Tus proyectos <span className="float-right">3</span></div>
                {projects.map(p => <Button key={p.name} variant="ghost" className={`nav-button ${project === p.name ? 'active' : ''}`} onClick={() => handleProjectClcik(p.name)}><span className={`project-dot ${p.tone}`} />{p.name}</Button>)}
                <div className="sidebar-bottom">
                    <Button variant="ghost" className="nav-button text-muted-foreground" onClick={onOpenHelp}><CircleHelp />Centro de ayuda<ArrowUpRight className="ml-auto" /></Button>
                    <div className="flex items-center gap-3 mt-4"><span className="avatar">RC</span><div><div className="text-xs font-semibold">Rubén Corona</div><div className="text-[10px] text-muted-foreground mt-1">Desarrollador</div></div></div>
                </div>
            </aside>
        </div>
    )
}
