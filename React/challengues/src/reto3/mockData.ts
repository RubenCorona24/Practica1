import type { Card } from "./interfaces";
import laptop from "./images/laptop.jpg";
import iphone from './images/iphone.png'
import ps5 from './images/ps5.jpg'
import lavadora from './images/lavadora.jpg'
import refrigerador from './images/refrigerador.jpg'
import airpods from './images/airpods.jpg'
import alexa from './images/alexa.jpg'
import mouse from './images/mouse.jpg'

export const defaultCards: Card[] = [
    { name: 'Laptop', image: laptop, price: 20000, category: 'electronics' },
    { name: 'Teléfono', image: iphone, price: 7000, category: 'electronics' },
    { name: 'PS5', image: ps5, price: 8900, category: 'electronics' },
    { name: 'Lavadora', image: lavadora, price: 15500, category: 'electronics' },
    { name: 'Refrigerador', image: refrigerador, price: 15000, category: 'electronics' },
    { name: 'AirPods', image: airpods, price: 1100, category: 'electronics' },
    { name: 'Alexa', image: alexa, price: 1900, category: 'electronics' },
    { name: 'Mouse Gamer', image: mouse, price: 1678, category: 'electronics' },

]