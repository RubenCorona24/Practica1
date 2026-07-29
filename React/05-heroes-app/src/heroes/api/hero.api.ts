import axios from 'axios'

//tomamos la base de URL de las variables de entorno
const baseURL = import.meta.env.VITE_API_URL

//creamos una instancia de axios
export const heroAPI = axios.create({
    baseURL: `${baseURL}/api/heroes`
})