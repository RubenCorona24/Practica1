
interface Props {
    title: string;
    subtitle: string
}

export const CustomHeader = ({ title, subtitle }: Props) => {
    return (
        <div>
            <header>{title}</header>
            <p>{subtitle}</p>
        </div>
    )
}
