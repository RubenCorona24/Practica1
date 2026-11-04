import { useMutation, useQueryClient } from "@tanstack/react-query"
import type { UserFormInformation } from "../interfaces/interface"
import { updateUserAction } from "../actions/updateUser.action"
import type { User } from "../UserCard"

interface UpdateVariables {
    id: number,
    data: UserFormInformation
}

export const useUpdateUser = () => {
    const queryClient = useQueryClient() //para actualizar caché 
    return useMutation({
        mutationFn: ({ data, id }: UpdateVariables) => updateUserAction(id, data),
        onSuccess: (updateUser) => {
            //Detalle del usuario
            queryClient.setQueryData(['user', updateUser.id], updateUser)
            //Reemplazar usuario en la lista
            queryClient.setQueryData<User[]>(["users"], (old = []) =>
                old.map(u => (u.id === updateUser.id ? updateUser : u)))
        }
    })
}
