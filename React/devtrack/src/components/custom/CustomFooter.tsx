
interface Props {
    leftMessage: string
    rightMessage?: string
}
export const CustomFooter = ({ leftMessage, rightMessage = "Vista de ejemplo" }: Props) => {
    return (
        <footer className="footer">
            <span>{leftMessage}</span>
            <span><span className="status-dot" />{rightMessage}</span>
        </footer>
    )
}
