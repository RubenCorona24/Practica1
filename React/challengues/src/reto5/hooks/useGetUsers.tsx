import { useQuery } from "@tanstack/react-query"
import { getUsers } from "../actions/getUsers.action."

export const useGetUsers = () => {

    return useQuery({
        queryKey: ['users'],
        queryFn: getUsers,
        staleTime: 60 * 1000 //6 segundos
    })
}
