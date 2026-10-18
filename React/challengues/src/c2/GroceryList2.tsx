import { Input } from "../components/ui/input"
import React, { useRef } from 'react'
import { Button } from "../components/ui/button"

import { useGroceryList } from "./hook/useGroceryList"



export const GroceryList2 = () => {
    const inputRef = useRef<HTMLInputElement>(null)
    const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
        if (e.key === "Enter") handleAdd()
    }

    const {
        products,
        filter,
        filteredProducts,
        pendingProducts,
        completedProducts,
        handleAddItem,
        handleRemoveItem,
        handleProductPurchased,
        setFilter
    } = useGroceryList()
    const handleAdd = () => {
        const value = inputRef.current?.value
        if (!value) return;
        if (handleAddItem(value)) { //si devuelve true
            inputRef.current!.value = ""; // Limpiar input
        }

    }

    return (
        <div>
            <h1>Lista de Compras </h1>
            <Input
                type="text"
                placeholder="Nombre del Producto"
                ref={inputRef}
                onKeyDown={handleKeyDown} />
            <br />
            <Button className={'cursor-pointer'} onClick={handleAdd}>Agregar al carrito</Button>
            {/*Contador de pendientes */}
            <p>
                {
                    pendingProducts === 0 ? "Todo comprado!!" : `Productos Pendientes: ${pendingProducts}`
                }
            </p>


            {/*Filtros*/}
            <div style={{ display: 'flex', gap: '8px' }}>
                <Button variant={filter === 'all' ? "default" : "outline"}
                    size={'sm'}
                    onClick={() => setFilter('all')}>
                    Todos ({products.length})
                </Button>
                <Button variant={filter === 'pending' ? "default" : "outline"}
                    size={'sm'}
                    onClick={() => setFilter('pending')}>
                    Pendientes ({pendingProducts})
                </Button>
                <Button variant={filter === 'completed' ? "default" : "outline"}
                    size={'sm'}
                    onClick={() => setFilter('completed')}>
                    Completados ({completedProducts})
                </Button>
            </div>

            {
                filteredProducts.length === 0 ? (
                    <p>Sin Productos para esta Categoría</p>) :
                    (
                        <ul>
                            {
                                filteredProducts.map(p => (
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
                    )
            }

            <br />
            {
                products.length === 0 ? (
                    <div>Sin Productos</div>
                ) : (
                    <div>Productos Totales: <span>{products.length}</span> </div>
                )
            }

        </div>
    )
}
