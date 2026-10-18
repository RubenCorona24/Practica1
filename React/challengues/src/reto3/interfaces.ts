export type Category = 'electronics' | 'clothing' | 'food'

export interface Card {
    name: string
    price: number
    image: string
    category: Category
}