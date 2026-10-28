import type { Card } from './interfaces'

import { Button } from "../components/ui/button"
import { Input } from "../components/ui/input"

import { useRef, useState } from 'react'
import { Badge } from '../components/ui/badge'
import {
    Select,
    SelectContent,
    SelectGroup,
    SelectItem,
    SelectLabel,
    SelectTrigger,
    SelectValue,
} from '../components/ui/select'

{/*Crear una tarjeta con nombre, precio e imagen.
Recibir los datos mediante props
Renderizar varias tarjetas desde un arreglo.
Extra: agregar una variante visual mediante props.*/}

const opciones = [
    { label: "Select a Category", value: null },
    { label: "electronics", value: "electronics" },
    { label: "clothing", value: "clothing" },
    { label: "food", value: "food" },
]
interface Props {
    cards: Card[]
    variant?: 'grid' | 'list'
}
export const ProductCard = ({ cards }: Props) => {
    const inputRef = useRef<HTMLInputElement>(null)
    const [category, setCategory] = useState<string | unknown>('all')
    const [search, setSearch] = useState('')
    //calcular productos filtrados
    const filteredProducts = cards.filter(c => c.name.toLowerCase().includes(search.trim().toLowerCase()))
        .filter(c => category === 'all' ? true : c.category === category)

    const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
        if (e.key === "Enter") setSearch(e.currentTarget.value)
    }
    return (
        <div className='p-6'>

            <h1 className="text-2xl font-bold mb-6"> Productos Disponibles</h1>
            <Input placeholder='Producto a buscar' ref={inputRef} onKeyDown={handleKeyDown} />
            <Select onValueChange={(value) => setCategory(value)}>
                <SelectTrigger className="w-full max-w-48">
                    <SelectValue />
                </SelectTrigger>
                <SelectContent>
                    <SelectGroup>
                        <SelectLabel>Categoría</SelectLabel>
                        <SelectItem value={'all'}>Todas</SelectItem>
                        {
                            opciones.filter(o => o.value)
                                .map(opcion => (
                                    <SelectItem key={opcion.value} value={opcion.value}>{opcion.label}</SelectItem>
                                ))
                        }
                    </SelectGroup>
                </SelectContent>
            </Select>

            {/*Mostrar filtros activos */}
            {category !== 'all' && (
                <Badge className='cursor-pointer'
                    onClick={() => setCategory('all')}>
                    {category}
                </Badge>
            )}
            <br /> <br />
            {/* Grid de productos */}
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
                {
                    filteredProducts.length === 0 ? (
                        <h3>Sin Productos</h3>
                    ) :
                        filteredProducts.map(card => (
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
                                    <Button className='w-full mt-2 cursor-pointer'
                                        onClick={() => console.log(`Click en ${card.name}`)}>Add to cart</Button>
                                    <Badge>{card.category}</Badge>
                                </div>

                            </div>
                        ))
                }
            </div>
        </div>
    )
}
