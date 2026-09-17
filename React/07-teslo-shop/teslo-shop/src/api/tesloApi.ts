//api de nuestra aplicación

import axios from 'axios'

const tesloApi = axios.create({
    baseURL: import.meta.env.VITE_API_URL, //extraemos nuetra URL 

})
//TODO: Interceptores

export { tesloApi }