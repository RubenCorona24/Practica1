import type { User } from "../interfaces/interface"

export const getUsers = async (): Promise<User[]> => {
    const response = await fetch("https://jsonplaceholder.typicode.com/users")
    if (!response.ok) {
        throw new Error(`Error ${response.status}: fallo al obtener usuarios`)
    }
    const data: User[] = await response.json()
    return data

}