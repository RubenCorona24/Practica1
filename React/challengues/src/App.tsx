//import { TaskController } from "./reto4/TasksController"
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { RouterProvider } from 'react-router'
import { router } from './reto5/route/router'
//import { GroceryList2 } from './c2/GroceryList2'
//QueryClient
const queryClient = new QueryClient()
export const App = () => {
    return (
        <QueryClientProvider client={queryClient}>

            < RouterProvider router={router} />
        </QueryClientProvider>
    )
}
