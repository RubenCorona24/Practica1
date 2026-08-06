
import { useNavigate } from 'react-router'
import type { MovieSearchResult } from '../interfaces/movie-search.interface'
import { Button } from '@base-ui/react'
import { Heart } from 'lucide-react'
import { useContext } from 'react'
import { FavoriteMovieContext } from '../context/FavoriteMovieContext'

interface Props {
    movie: MovieSearchResult
}



export const MovieGridCard = ({ movie }: Props) => {
    //consumir el FavoriteContext
    const { isFavorite, toggleFavorite } = useContext(FavoriteMovieContext)
    const navigate = useNavigate()
    const handleClick = () => {
        navigate(`/movie/${movie.id}`)
    }

    return (

        // ---------- 8.1 Tarjeta individual de película ----------
        <article
            onClick={handleClick}
            className="group relative overflow-hidden rounded-xl bg-card ring-1 ring-border transition-transform duration-300 hover:-translate-y-1.5 hover:shadow-[var(--shadow-glow)] cursor-pointer"
        >
            <div className="relative aspect-[2/3] overflow-hidden">
                <img
                    src={movie.poster}
                    alt={`Póster de ${movie.title}`}
                    width={600}
                    height={900}

                    className="h-full w-full object-cover transition-transform duration-500 group-hover:scale-105"
                />
                <div className="absolute inset-0 bg-[image:var(--gradient-fade)]" />
                {/*<span className="absolute right-2 top-2 inline-flex items-center gap-1 rounded-full bg-background/70 px-2.5 py-1 text-xs font-semibold text-accent backdrop-blur">
                            <Star className="size-3 fill-current" />
                            {movie.rating.toFixed(1)}
                        </span>}*/}
                <div className="absolute inset-x-0 bottom-0 p-4">
                    <h3 className="font-display text-2xl leading-none tracking-wide text-foreground">
                        {movie.title}
                    </h3>
                    <p className="mt-1 text-xs uppercase tracking-[0.18em] text-muted-foreground">
                        {movie.year} · {/*movie.duration*/}
                    </p>
                    {/* <p className="mt-2 max-h-0 overflow-hidden text-sm text-muted-foreground opacity-0 transition-all duration-300 group-hover:max-h-24 group-hover:opacity-100">
                                {movie.synopsis}
                            </p>*/}
                    <Button size="sm" variant="ghost" className="absolute bottom-3 right-3 bg-white/90 hover:bg-white"
                        onClick={() => toggleFavorite(movie)}>
                        <Heart className={`h-4 w-4 ${isFavorite(movie) ? 'fill-red-500' : 'text-gray-500'
                            }`} />
                    </Button>
                </div>
            </div>
            {/* <div className="flex flex-wrap gap-1.5 p-3">
                        {movie.genres.map((g) => (
                            <span
                                key={g}
                                className="rounded-full bg-secondary px-2.5 py-0.5 text-[11px] font-medium text-secondary-foreground"
                            >
                                {g}
                            </span>
                        ))}
                    </div>*/}
        </article>

    )
}
