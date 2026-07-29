import { heroAPI } from "../api/hero.api"
import type { HeroesResponse } from "../interfaces/get-heroes.response";

const BASE_URL = import.meta.env.VITE_API_URL
//devuelve promesa tipo 'HeroesResponse' ya declarada en 'interfaces/get-heroes.response.ts'
export const getHeroesByPage = async (): Promise<HeroesResponse> => {
    const { data } = await heroAPI.get<HeroesResponse>('/')
    const heroes = data.heroes.map(hero => ({
        ...hero,
        image: `${BASE_URL}/images/${hero.image}` //url para ver la imagen
    }))
    return { //retornamos la data
        ...data,
        heroes //retornamos los heroes
    }
}