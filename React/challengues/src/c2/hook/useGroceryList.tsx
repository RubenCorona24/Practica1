import { useState } from "react"
import { defaultMockProducts, type Filter, type Product } from "../interface"


export const useGroceryList = () => {
    const [products, setProducts] = useState(defaultMockProducts)
    const [filter, setFilter] = useState<Filter>('all')
    const handleAddItem = (productName: string) => {
        const value = productName.trim()
        //Validar existencia de producto
        if (!value) return;
        //Evitar duplicados
        if (products.some(p => p.name.toLowerCase() === value.toLowerCase())) return;
        //Crear nuevo producto
        const newProduct: Product = {
            id: Date.now(),
            name: value,
            purchased: false
        }
        //Añadir nuevo producto a productos
        setProducts([...products, newProduct])
        //Resetear el input
    }
    const handleRemoveItem = (id: number) => {
        //Filtrar para eliminar
        const newProducts = products.filter(p => p.id !== id)
        setProducts(newProducts)
    }
    const handleProductPurchased = (id: number) => {
        setProducts(prev => prev.map(p =>
            p.id === id ? { ...p, purchased: !p.purchased } : p
        ))
    }
    //Conteo de productos pendientes
    const pendingProducts = products.filter(p => p.purchased === false).length

    //Filtro de productos
    const filteredProducts = products.filter(p => {
        if (filter === 'pending') return !p.purchased //retorna productos no comprados
        if (filter === 'completed') return p.purchased //retorna producctos comprados
        return true
    })

    return {
        //values
        products,
        filter,
        //methods (Funciones para modificar el estado)
        handleAddItem,
        handleRemoveItem,
        handleProductPurchased,
        //Datos calculados
        filteredProducts,
        pendingProducts
    }
}
