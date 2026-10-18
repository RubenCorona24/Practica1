import type { Card } from './interfaces'

import { Button } from "../components/ui/button"
import { Input } from "../components/ui/input"

import { useRef, useState } from 'react'

{/*Crear una tarjeta con nombre, precio e imagen.
Recibir los datos mediante props
Renderizar varias tarjetas desde un arreglo.
Extra: agregar una variante visual mediante props.*/}

interface Props {
    cards: Card[]
    variant?: 'grid' | 'list'
}
export const ProductCard = ({ cards }: Props) => {
    const inputRef = useRef<HTMLInputElement>(null)
    const [products, setCards] = useState<Card[]>(cards)
    const handleSearch = (value: string) => {
        const search = value.trim().toLowerCase();
        if (!search) {
            setCards(cards);
            return;
        }

        const newProducts = cards.filter(p => p.name.toLowerCase().includes(search))
        setCards(newProducts)
    }
    const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
        if (e.key === "Enter") handleSearch(e.currentTarget.value)
    }
    return (
        <div className='p-6'>

            <h1 className="text-2xl font-bold mb-6"> Productos Disponibles</h1>
            <Input placeholder='Producto a buscar' ref={inputRef} onKeyDown={handleKeyDown} />
            <br /> <br />
            {/* Grid de productos */}
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
                {
                    cards.map(card => (
                        <div key={card.name} className="bg-white rounded-xl shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">
                            {/*Imagen controlada */}
                            <div className="w-full h-48 overflow-hidden">
                                <img
                                    src={card.image}
                                    alt={card.name}
                                    className='w-full h-full object-cover hover:scale-105 transition-transform duration-300' />

                            </div>
                            {/*Información del producto */}
                            <div className='p-4'>
                                <p className='font-medium text-gray-800 truncate'>{card.name}</p>
                                <p className='text-blue-600 font-bold mt-1'>${card.price}</p>
                                <Button className='w-full mt-2 cursor-pointer'>Add to cart</Button>
                            </div>

                        </div>
                    ))
                }
            </div>
        </div>
    )
}
