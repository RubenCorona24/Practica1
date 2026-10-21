
import { Button } from '@/components/ui/button'
import { Bell, Search, X } from 'lucide-react'

interface Props {
    search: string;
    onSearchChanged: (query: string) => void
    onOpenNotifications: () => void;
}

export const Topbar = ({ search, onSearchChanged, onOpenNotifications }: Props) => {
    const handleInputChanged = (e: React.ChangeEvent<HTMLInputElement>) => {
        onSearchChanged(e.target.value)
    }
    return (
        <header className="topbar">
            <div className="search">
                <Search size={17} />
                <input
                    aria-label="Buscar proyectos y tareas"
                    placeholder="Buscar proyectos, tareas..."
                    value={search}
                    onChange={handleInputChanged}
                />
                {search && (
                    <Button variant="ghost" size="icon" title="Limpiar búsqueda" onClick={() => onSearchChanged('')}>
                        <X />
                    </Button>
                )}
            </div>

            <div className="flex items-center gap-4">
                <Button variant="ghost" size="icon" title="Notificaciones" onClick={onOpenNotifications}>
                    <Bell />
                </Button>
                <span className="h-6 border-l border-border" />
                <span className="avatar">RC</span>
            </div>
        </header>
    )
}
