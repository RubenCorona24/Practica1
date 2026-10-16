
import { Button } from "../components/ui/button"
import { defaultProducts } from "./interface"
import { Input } from "../components/ui/input"
import { useRef, useState } from "react"


export const GroceryList = () => {
    const inputRef = useRef<HTMLInputElement>(null)
    const [products, setProducts] = useState<string[]>(defaultProducts)
    //Función agregar producto
    const handleAddItem = () => {
        if (!inputRef.current?.value) return;
        const newProduct = inputRef.current.value.trim()
        //Evitar items duplicados
        if (products.some(p => p.toLowerCase() === newProduct.toLowerCase())) return;
        const newProducts = [...products, newProduct]
        setProducts(newProducts)
        //Resetear el valor 
        inputRef.current.value = ""
    }
    const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
        if (e.key === 'Enter') handleAddItem()


    }
    //Función eliminar producto
    const handleRemoveItem = (productName: string) => {
        const newProducts = products.filter(p => p !== productName)
        setProducts(newProducts)
    }
    //Función de agregar 
    return (
        <div>
            <h1>Grocery List</h1>
            <Input
                type="text"
                placeholder="Nombre del Producto"
                ref={inputRef}
                onKeyDown={handleKeyDown} />
            <br />
            <Button className={'cursor-pointer'} onClick={handleAddItem}>Agregar al carrito</Button>
            <br /><br />
            <hr />
            <br />
            {
                products.length === 0 ? (
                    <div>Sin Productos</div>
                ) : <div>Productos Disponibles: <span>{products.length}</span></div>
            }
            <br />
            <ul>
                {
                    products.map(product => (
                        <li key={product} style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
                            {product}
                            <Button onClick={() => handleRemoveItem(product)}>Remover Item</Button>
                        </li>
                    ))
                }
            </ul>
        </div>
    )
}
