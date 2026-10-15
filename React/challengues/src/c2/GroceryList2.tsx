import { Input } from "../components/ui/input"
import React, { useRef, useState } from 'react'
import { defaultMockProducts } from './mockdata'
import { Button } from "../components/ui/button"

import { type Product } from './mockdata'



export const GroceryList2 = () => {
    const [products, setProducts] = useState(defaultMockProducts)
    const inputRef = useRef<HTMLInputElement>(null)
    const handleAddItem = () => {
        const value = inputRef.current?.value.trim()
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
        inputRef.current!.value = ""
    }
    //Función de eliminar producto
    const handleRemoveItem = (id: number) => {
        //Filtrar para eliminar
        const newProducts = products.filter(p => p.id !== id)
        setProducts(newProducts)
    }
    const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
        if (e.key === "Enter") handleAddItem()
    }
    //Función de setear el comprado
    const handleProductPurchased = (id: number) => {
        setProducts(prev => prev.map(p =>
            p.id === id ? { ...p, purchased: !p.purchased } : p
        ))
    }
    //Conteo de productos pendientes
    const pendingProducts = products.filter(p => p.purchased === false).length


    return (
        <div>
            <h1>Grocery List 2</h1>
            <Input
                type="text"
                placeholder="Nombre del Producto"
                ref={inputRef}
                onKeyDown={handleKeyDown} />
            <br />
            <Button className={'cursor-pointer'} onClick={handleAddItem}>Agregar al carrito</Button>
            {
                products.length === 0 ? (
                    <div>Sin Productos</div>
                ) : (
                    <div>Productos Totales: <span>{products.length}</span> </div>
                )
            }
            <ul>
                {
                    products.map(p => (
                        <li key={p.id}
                            style={{
                                display: 'flex',
                                gap: '8px',
                                alignItems: 'center',
                                // ✅ tachado si está comprado
                                textDecoration: p.purchased ? 'line-through' : 'none',
                                opacity: p.purchased ? 0.5 : 1
                            }}>
                            {p.name}
                            <Input type='checkbox' checked={p.purchased}
                                onChange={() => handleProductPurchased(p.id)} />
                            <Button
                                variant={'destructive'}
                                onClick={() => handleRemoveItem(p.id)}
                                className={'cursor-pointer'}>Eliminar</Button>
                        </li>
                    ))
                }
            </ul>
            <br />
            <div>Productos Pendientes: <span>{pendingProducts}</span></div>
        </div>
    )
}
