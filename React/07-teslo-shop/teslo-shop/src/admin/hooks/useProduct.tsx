import { getProductByIdAction } from "../actions/get-product-by-id.action"
import { useQuery } from '@tanstack/react-query'

export const useProduct = (id: string) => { //recibo id del producto
    //tanStackQuery para peticiones http
    return useQuery({
        queryKey: ['product', id],
        queryFn: () => getProductByIdAction(id), //acción mandando id,
        retry: false,
        staleTime: 1000 * 60 * 5,
    })
    //TODO: mutación
}
