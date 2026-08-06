
//custom que regresa informacion de la API

import { useQuery } from "@tanstack/react-query"
import { getMovieAction } from "../actions/get-movie.action"

export const useMovie = (id: string) => {
    return useQuery({
        queryKey: ['movie', id], //dependencias
        queryFn: () => getMovieAction(id),
        staleTime: 1000 * 60 * 5 //5 segundos
    })
}