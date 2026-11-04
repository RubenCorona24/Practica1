import { useNavigate, useParams } from "react-router"
import { useCreateUser } from "./hooks/useCreateUser"
import { useUpdateUser } from "./hooks/useUpdateUser"
import { useGetUser } from "./hooks/useGetUser"
import type { UserFormInformation } from "./interfaces/interface"
import { UserForm } from "./form/UserForm"

export const UserFormPage = () => {
    const { id } = useParams()
    const navigate = useNavigate()
    const isNew = id === undefined || id === "new"

    //hooks de mutation
    const createUser = useCreateUser()
    const updateUser = useUpdateUser()
    const { data: user, isLoading } = useGetUser(Number(id), { enabled: !isNew })
    if (!isNew && isLoading) return <p>Cargando Información...</p>
    if (!isNew && !user) return <p>Usuario no encontrado...</p>
    const handleSubmit = (data: UserFormInformation) => {
        if (isNew) {
            createUser.mutate(data, { onSuccess: () => navigate("/") })
        } else {
            updateUser.mutate({ id: Number(id), data }, { onSuccess: () => navigate("/") })
        }

    }
    const defaultValues: Partial<UserFormInformation> | undefined = user && {
        name: user.name,
        username: user.username,
        email: user.email,
        phone: user.phone,
        website: user.website,
        city: user.address.city,
    }
    return (
        <UserForm
            defaultValues={isNew ? undefined : defaultValues}
            onSubmit={handleSubmit}
            isPending={createUser.isPending || updateUser.isPending}
        />
    )
}
