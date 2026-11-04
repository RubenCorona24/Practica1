import { useQuery } from "@tanstack/react-query"
import { getUser } from "../actions/getUser.action"

export const useGetUser = (userId: number, options?: { enabled?: boolean }) => {
    return useQuery({
        queryKey: ['user', userId],
        queryFn: () => getUser(userId),
        staleTime: 1000 * 60 * 5,
        enabled: options?.enabled ?? !Number.isNaN(userId)
    })
}
