import { useMutation, useQueryClient } from "@tanstack/react-query"
import { createUserAction } from "../actions/createUser.action"
import type { User } from "../UserCard"

export const useCreateUser = () => {
    const queryClient = useQueryClient() //para actualizar caché 
    return useMutation({
        mutationFn: createUserAction,
        onSuccess: (newUser) => {
            //agregar el nuevo usuario a la lista en caché
            queryClient.setQueryData<User[]>(['users'], (old = []) => [...old, newUser])
            queryClient.setQueryData(["user", newUser.id], newUser)
        }
    })
}
