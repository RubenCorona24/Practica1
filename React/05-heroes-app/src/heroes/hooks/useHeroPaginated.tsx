import { useQuery } from '@tanstack/react-query'
import { getHeroesByPage } from '../actions/get-heroes-by-page.action'


export const useHeroPaginated = (limit: string, page: string) => {
    return useQuery({
        queryKey: ['heroes', { page, limit }],
        //funcion de query key recibe argumentos => mismos en el queryKey
        queryFn: () => getHeroesByPage(+page, +limit),
        staleTime: 1000 * 60 * 5 //5 minutos
    })
}
