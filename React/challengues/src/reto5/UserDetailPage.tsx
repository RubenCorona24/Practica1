import { useParams } from "react-router"

import { useGetUser } from "./hooks/useGetUser"
import { UserCard } from "./UserCard"

export const UserDetailPage = () => {
    const { id } = useParams() //leemos id de parámetros
    const idUser = Number(id)
    const { data: user, isLoading, isError } = useGetUser(idUser)
    if (isLoading) return <p>Cargando usuario...</p>
    if (isError) return <p>Error al cargar usuario X</p>
    if (!user) return <p>Usuario no encontrado</p>
    return (
        <UserCard user={user} />
    )
}
