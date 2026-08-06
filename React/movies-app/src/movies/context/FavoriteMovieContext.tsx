import { createContext, useEffect, useState, type PropsWithChildren } from 'react'
import type { MovieSearchResult } from '../interfaces/movie-search.interface';

interface FavoriteMovieContextProps {
    favorites: MovieSearchResult[],
    favoriteCount: number;

    isFavorite: (movie: MovieSearchResult) => boolean
    toggleFavorite: (movie: MovieSearchResult) => void;


}

export const FavoriteMovieContext = createContext({} as FavoriteMovieContextProps)


//Provider
export const FavoriteMovieProvider = ({ children }: PropsWithChildren) => {
    const [favorites, setFavorites] = useState<MovieSearchResult[]>([])
    const toggleFavorite = (movie: MovieSearchResult) => {
        const exists = favorites.find(favorite => favorite.id === movie.id)
        if (!exists) {
            setFavorites([...favorites, movie])
            return;
        }
        //si existe en favoritos
        const filteredFavorites = favorites.filter(favorite => favorite.id !== movie.id)
        setFavorites(filteredFavorites)
    }

    //useEffect de cuando los favoritos cambian
    useEffect(() => {
        localStorage.setItem("favorites", JSON.stringify(favorites))
    }, [favorites]) //dependencias => favorites
    return (
        <FavoriteMovieContext value={{
            favorites,
            favoriteCount: favorites.length,
            isFavorite: (movie: MovieSearchResult) => favorites.some(favorite => favorite.id === movie.id),
            toggleFavorite
        }}>
            {children} {/*dentro el children */}
        </FavoriteMovieContext>
    )

}