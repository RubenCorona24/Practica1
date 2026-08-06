
interface Props {
    subtitle?: string;
    title: string;
    description?: string
}

export const CustomHeader = ({ title, description, subtitle = "Función de la semana" }: Props) => {
    return (
        <div className="relative mx-auto max-w-6xl px-5 py-24 sm:py-32">
            <p className="text-xs uppercase tracking-[0.35em] text-accent">{subtitle}</p>
            <h1 className="mt-4 max-w-3xl font-display text-6xl leading-[0.9] tracking-wide text-foreground sm:text-8xl">
                {title}
            </h1>
            <p className="">
                {description}
            </p>
        </div>
    )
}
