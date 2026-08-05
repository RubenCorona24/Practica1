import { movieAPI } from "../api/movie.api"

export const getMovieAction = async (query: string) => {
    const { data } = await movieAPI.get("", {
        params: {
            "t": query
        }
    })
    return data
}