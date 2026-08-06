import { QueryClient, QueryClientProvider } from "@tanstack/react-query"
import { RouterProvider } from "react-router"
import { appRouter } from "./router/app.router"
import { FavoriteMovieProvider } from "./movies/context/FavoriteMovieContext"

//configurar el cliente con queryClient
const queryClient = new QueryClient()
export const MoviesApp = () => {
    return (
        <QueryClientProvider client={queryClient}>
            <FavoriteMovieProvider>
                <RouterProvider router={appRouter} />
            </FavoriteMovieProvider>
        </QueryClientProvider>
    )
}
