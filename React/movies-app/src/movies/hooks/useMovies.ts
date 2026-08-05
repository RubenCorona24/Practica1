import { useQuery } from "@tanstack/react-query"
import { getMoviesAction } from "../actions/get-movies.action"

export const useMovies = () => {
    return useQuery({
        queryKey: ['movies'],
        queryFn: getMoviesAction,
        staleTime: 1000 * 6 * 5 //5 minutos
    })
}