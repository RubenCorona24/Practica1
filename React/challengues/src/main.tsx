import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
//import { App } from './App.tsx'
//import { CounterApp } from './C1/components/CounterApp.tsx'
//import { GroceryList } from './c2/GroceryList.tsx'
import { GroceryList2 } from './c2/GroceryList2.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    {/*<CounterApp initialValue={2} steps={5} />*/}
    <GroceryList2 />
  </StrictMode>,
)
