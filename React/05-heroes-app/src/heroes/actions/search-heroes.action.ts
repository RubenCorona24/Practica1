import { heroAPI } from "../api/hero.api";
import type { Hero } from "../interfaces/hero.interface";

//interfaz de opciones
interface Options {
    name?: string;
    team?: string;
    category?: string;
    universe?: string;
    status?: string;
    strength?: string;
}
const BASE_URL = import.meta.env.VITE_API_URL
//acción de buscar héroes
export const searchHeroesAction = async ({ name, team, category, status, strength, universe }: Options) => {
    if (!name && !team && !category && !status && !strength && !universe) {
        return [] //retornamos arreglo vacío
    }   
    const { data } = await heroAPI.get<Hero[]>(`/search`, {
        params: {
            name, team, category, status, strength, universe
        }
    })

    return data.map(hero => ({
        ...hero,
        image: `${BASE_URL}/images/${hero.image}`
    }))
}