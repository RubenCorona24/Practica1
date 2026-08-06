import { MovieGridCard } from './MovieGridCard'
import type { MovieSearchResult } from '../interfaces/movie-search.interface'
interface Props { //recibe un arreglo de heroes 
    movies: MovieSearchResult[]
}

export const MovieGrid = ({ movies }: Props) => {
    //consumir el useMovie 

    return (

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-8">

            {
                movies.map(movie => (
                    <MovieGridCard key={movie.id}
                        movie={movie} />
                ))
            }

        </div>
    )
}