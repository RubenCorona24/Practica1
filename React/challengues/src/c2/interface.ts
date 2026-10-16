
export const defaultProducts = [
    'Manzana', 'Plátano', 'Lechuga'
]

//Interfaz para GroceryList2
export interface Product {
    id: number
    name: string
    purchased: boolean
}

//Productos por defecto
export const defaultMockProducts: Product[] = [
    { id: 1, name: "Leche", purchased: false },
    { id: 2, name: "Manzanas", purchased: false },
    { id: 3, name: "Verduras", purchased: false },
    { id: 4, name: "Yogur", purchased: false },
    { id: 5, name: "Frijoles", purchased: false },
]

//tipo de filtro
export type Filter = "all" | "pending" | "completed"