import type { User } from "../interfaces/interface";

export const getUser = async (userId: number): Promise<User> => {
    const res = await fetch(`https://jsonplaceholder.typicode.com/users/${userId}`)
    if (!res.ok) throw new Error("Error al cargar usuario")
    const data = await res.json()
    return data
}