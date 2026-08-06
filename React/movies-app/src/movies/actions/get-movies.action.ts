import { movieAPI } from "../api/movie.api"
import type { MoviesResponse } from "../interfaces/get-movies.response"
import type { MovieSearchResult } from "../interfaces/movie-search.interface"

//función para extraer una lista de películas
export const getMoviesAction = async (): Promise<MovieSearchResult[]> => {
    const { data } = await movieAPI.get<MoviesResponse>("", { params: { s: 'love' } })
    const result = data.Search.map(movie => ({
        id: movie.imdbID,
        title: movie.Title,
        poster: movie.Poster,
        year: Number(movie.Year),

    }))
    console.log('movies transformados:', result)
    console.log('algún id undefined?', result.some(m => m.id === undefined))

    return result
}