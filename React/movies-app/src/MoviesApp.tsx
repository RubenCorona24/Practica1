import { QueryClient, QueryClientProvider } from "@tanstack/react-query"
import { RouterProvider } from "react-router"
import { appRouter } from "./router/app.router"

//configurar el cliente con queryClient
const queryClient = new QueryClient()
export const MoviesApp = () => {
    return (
        <QueryClientProvider client={queryClient}>
            <RouterProvider router={appRouter} />
        </QueryClientProvider>
    )
}
