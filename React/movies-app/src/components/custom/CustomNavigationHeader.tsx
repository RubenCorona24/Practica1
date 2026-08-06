import { Clapperboard } from 'lucide-react'

interface Props {
    title: string
}
export const CustomNavigationHeader = ({ title }: Props) => {
    return (
        <header className="sticky top-0 z-50 border-b border-border/60 bg-background/80 backdrop-blur-xl">
            <nav className="mx-auto flex max-w-6xl items-center justify-between px-5 py-4">
                <a href="/" className="flex items-center gap-2">
                    <Clapperboard className="size-6 text-primary" />
                    <span className="font-display text-2xl tracking-[0.12em] text-foreground">
                        CINEVERSO
                    </span>
                </a>
                <span className="rounded-full bg-secondary px-4 py-2 text-sm text-foreground">
                    {title}
                </span>
            </nav>
        </header>
    )
}
