
interface Props {
    title: string;
    description?: string
}

export const CustomHeader = ({ title, description }: Props) => {
    return (
        <div className="relative mx-auto max-w-6xl px-5 py-24 sm:py-32">
            <p className="text-xs uppercase tracking-[0.35em] text-accent">Función de la semana</p>
            <h1 className="mt-4 max-w-3xl font-display text-6xl leading-[0.9] tracking-wide text-foreground sm:text-8xl">
                {title}
            </h1>
            <p className="mt-5 max-w-xl text-base text-muted-foreground">
                {description}
            </p>
        </div>
    )
}
