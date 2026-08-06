import { createContext, useEffect, useState, type PropsWithChildren } from 'react'
import type { Hero } from '../interfaces/hero.interface';

interface FavoriteHeroContext {
    //State
    favorites: Hero[];
    favoriteCount: number;



    //Methods
    isFavorite: (hero: Hero) => boolean;
    toggleFavorite: (hero: Hero) => void;


}

export const FavoriteHeroContext = createContext({} as FavoriteHeroContext); //create the context

//obtener favoritos del localStorage
const getFavoritesFromLocalStorage = (): Hero[] => {
    const favorites = localStorage.getItem("favorites")
    return favorites ? JSON.parse(favorites) : []
}

//create the component (provider)
export const FavoriteHeroProvider = ({ children }: PropsWithChildren) => {

    const [favorites, setFavorites] = useState<Hero[]>(getFavoritesFromLocalStorage()) //inicializamos con favorites del localStorage "o arreglo vacío"
    const toggleFavorite = (hero: Hero) => {
        const heroExists = favorites.find(h => h.id === hero.id)
        if (heroExists) {
            //eliminamos al heroe
            const filterFavorites = favorites.filter(h => h.id !== hero.id)
            setFavorites(filterFavorites)
            return;
        }
        setFavorites([...favorites, hero])

    }
    //useEffect to update favorites when favorites change
    useEffect(() => {
        localStorage.setItem("favorites", JSON.stringify(favorites)) //en modo JSON.stringify
    }, [favorites])
    return (
        <FavoriteHeroContext value={{
            //values
            favorites: favorites,
            favoriteCount: favorites.length,
            //methods
            isFavorite: (hero: Hero) => favorites.some(h => h.id === hero.id),
            toggleFavorite: toggleFavorite
        }}>

            {children}
        </FavoriteHeroContext>
    )

}


