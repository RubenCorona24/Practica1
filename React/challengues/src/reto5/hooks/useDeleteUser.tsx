import { useMutation, useQueryClient } from "@tanstack/react-query"
import { deleteUserAction } from "../actions/deleteUser.action"
import type { User } from "../UserCard"

export const useDeleteUser = () => {
    const queryClient = useQueryClient() //para actualizar caché 
    return useMutation({
        mutationFn: deleteUserAction,
        onSuccess: (_, id) => {
            queryClient.setQueryData<User[]>(["users"], (old = []) =>
                old.filter(u => u.id !== id))
        }
    })
}
