import { heroAPI } from "../api/hero.api"
import type { Hero } from "../interfaces/hero.interface"

const BASE_URL = import.meta.env.VITE_API_URL


export const getHeroAction = async (idSlug: string) => { //recibimos nombre tipo string
    const { data } = await heroAPI.get<Hero>(`/${idSlug}`)
    return {
        ...data,
        image: `${BASE_URL}/images/${data.image}`
    }
}