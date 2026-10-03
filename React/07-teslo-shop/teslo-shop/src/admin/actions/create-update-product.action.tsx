//acción de crear o actualizar un producto

import { tesloApi } from "@/api/tesloApi";
import type { Product } from "@/interfaces/product.interface";
import { sleep } from "@/lib/sleep";

export const createUpdateProductAction = async (productLike: Partial<Product>): Promise<Product> => {
    await sleep(1500)
    //extraer información del productLike
    const { id, user, images = [], ...rest } = productLike;

    const isCreating = id === "new"
    //transformar strings a números
    rest.price = Number(rest.price || 0)
    rest.stock = Number(rest.stock || 0)
    //endpoint para actualizar info de producto (PATCH o POST dependiendo del isCreating)
    const { data } = await tesloApi({
        url: isCreating ? '/products' : `/products/${id}`,
        method: isCreating ? 'POST' : 'PATCH',
        data: rest
    })
    //reconstruir la data con las imágenes
    const imagesWithUrl = data.images.map((img: string | string[]) => {
        if (img.includes("htttp")) return img;
        return `${import.meta.env.VITE_API_URL}/files/product/${img}`
    })
    return {
        ...data,
        images: imagesWithUrl
    }
}