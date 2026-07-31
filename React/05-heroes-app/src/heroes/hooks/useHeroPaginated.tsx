import { useQuery } from '@tanstack/react-query'
import { getHeroesByPage } from '../actions/get-heroes-by-page.action'


export const useHeroPaginated = (limit: string, page: string, category: string = "all") => {
    return useQuery({
        queryKey: ['heroes', { page, limit, category }],
        //funcion de query key recibe argumentos => mismos en el queryKey
        queryFn: () => getHeroesByPage(+page, +limit, category),
        staleTime: 1000 * 60 * 5 //5 minutos
    })
}
