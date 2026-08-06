import { movieAPI } from "../api/movie.api"
import type { MovieDetailData } from "../interfaces/movie-detail.interface"

export const getMovieAction = async (id: string): Promise<MovieDetailData> => {
    const { data } = await movieAPI.get<MovieDetailData>("", {
        params: {
            i: id
        }
    })
    if (data.Response === "False") {
        throw new Error("Error al extraer información de película")
    }
    return data
}