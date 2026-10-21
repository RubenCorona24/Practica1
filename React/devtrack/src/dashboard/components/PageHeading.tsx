import { Button } from "@/components/ui/button";
import { ChevronRight, Plus } from "lucide-react";

interface Props {
    onNewTask: () => void;
}
export const PageHeading = ({ onNewTask }: Props) => {
    return (
        <div className="page-heading">
            <div>
                <div className="flex items-center gap-2 text-[11px] text-muted-foreground mb-3">
                    <span>Workspace</span>
                    <ChevronRight size={12} />
                    <span className="text-foreground">Dashboard</span>
                </div>
                <h1>Buen día, Rubén <span className="text-xl">✦</span></h1>
                <p className="subtext mt-1">Vamos a construir algo increíble hoy.</p>
            </div>
            <Button className="mt-8" onClick={onNewTask}>
                <Plus />Nueva tarea
            </Button>
        </div>
    )
}
