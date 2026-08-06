
//accion de extraer peliculas buscadas

import { movieAPI } from "../api/movie.api"
import type { MoviesResponse } from "../interfaces/get-movies.response"
import type { MovieSearchResult } from "../interfaces/movie-search.interface"



export const searchMoviesAction = async (title: string): Promise<MovieSearchResult[]> => {
    if (!title) {
        return []
    }
    const { data } = await movieAPI.get<MoviesResponse>("", {
        params: {
            s: title
        }
    })
    if (data.Response === "False") {
        return []
    }
    return data.Search.map(movie => ({
        id: movie.imdbID,
        title: movie.Title,
        poster: movie.Poster,
        year: Number(movie.Year)
    }))
}