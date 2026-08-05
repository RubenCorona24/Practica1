//creamos instancia de axios para ser utilizada en funciones de extraer API
import axios from 'axios'

const BASE_URL = import.meta.env.VITE_API_URL
const API_KEY = import.meta.env.VITE_API_KEY
export const movieAPI = axios.create({
    baseURL: `${BASE_URL}`,
    params: {
        apikey: API_KEY
    }
})