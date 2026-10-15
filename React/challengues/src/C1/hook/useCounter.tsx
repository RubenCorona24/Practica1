import { useState } from "react"

export const useCounter = (initialValue: number = 1, step: number = 1) => {
    const [value, setValue] = useState(initialValue)
    const handleIncrement = () => {
        setValue(currentValue => currentValue + step)
    }
    const handleDecrement = () => {
        if (value - step < 0) return;
        setValue(currentValue => currentValue - step)
    }
    const handleReset = () => {
        setValue(initialValue)
    }
    return {
        //values
        value,
        //methods
        handleIncrement,
        handleDecrement,
        handleReset

    }
}
