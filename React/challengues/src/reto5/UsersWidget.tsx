import { useGetUsers } from "./hooks/useGetUsers"
import { UsersGridCard } from "./UsersGridCard"
import { Input } from "../components/ui/input"
import { useState } from "react"
import { Badge } from '../components/ui/badge'
export const UsersWidget = () => {
    const [search, setsearch] = useState('')
    //TODO: Implementar Practicas: useEffect, async/await, peticiones HTTP y estados de carga.
    //consumir el useGetUsers
    const { data: users = [], isLoading, isError } = useGetUsers()
    if (isLoading) {
        return <p>Cargando usuarios...</p>
    }
    if (isError) {
        return <p>Error al cargar usuarios</p>
    }
    const filteredUsers = users.filter(user => user.username.toLowerCase().includes(search.trim().toLowerCase()))

    return (
        <div className="container">
            <h1 className="header">Company Users</h1>
            <Input placeholder="Nombre de Usuario"
                type="text"
                onChange={(e) => setsearch(e.target.value)} />

            {
                filteredUsers.length === 0 ? (
                    <Badge variant="destructive">Sin usuarios</Badge>) : <UsersGridCard users={filteredUsers} />
            }

        </div>

    )
}
