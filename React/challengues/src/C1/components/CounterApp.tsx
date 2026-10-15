import { Button } from "../../components/ui/button"
import { useCounter } from "../hook/useCounter"

interface Props {
    initialValue: number
    steps: number
}

export const CounterApp = ({ initialValue, steps }: Props) => {
    const { value, handleIncrement, handleDecrement, handleReset } = useCounter(initialValue, steps)
    return (
        <div>
            <h1>Counter App</h1>
            <span>{value}</span>
            <br /><br />
            <Button onClick={handleIncrement} className={'cursor-pointer'}>Incrementar</Button>
            <Button onClick={handleDecrement} className={'cursor-pointer'}>Decrementar</Button>
            <Button onClick={handleReset} className={'cursor-pointer'}>Resetear</Button>
        </div>
    )
}
