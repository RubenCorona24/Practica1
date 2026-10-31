import { useQuery } from "@tanstack/react-query"
import { getUser } from "../actions/getUser.action"

export const useGetUser = (userId: number) => {
    return useQuery({
        queryKey: ['user', userId],
        queryFn: () => getUser(userId),
        staleTime: 6 * 1000
    })
}
