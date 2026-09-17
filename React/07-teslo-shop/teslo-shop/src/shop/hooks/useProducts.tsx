//custom hook para extraer la data de los productos

import { useQuery } from '@tanstack/react-query'
import { getProductsAction } from '../actions/getProducts.action'
import { useSearchParams } from 'react-router'
export const useProducts = () => {
    //TODO: Viene lógica
    const [searchParams] = useSearchParams()
    //tomamos lo que ocupamos del searchParams (limit & offset)
    const limit = searchParams.get("limit") ?? 9;
    const page = searchParams.get("page") ?? 1;
    //calculamos el offset
    const offset = (Number(page) - 1) * Number(limit)
    return useQuery({
        queryKey: ['products', { limit, offset }],
        queryFn: () => getProductsAction({
            limit: isNaN(+limit) ? 9 : limit,
            offset: isNaN(offset) ? 0 : offset
        }),
        staleTime: 1000 * 60 * 5
    })
}
