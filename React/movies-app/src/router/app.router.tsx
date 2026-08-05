import { createBrowserRouter } from "react-router";
import { HomePage } from "../movies/pages/home/HomePage";
import { MoviesLayout } from "../movies/layout/MoviesLayout";
import { SearchPage } from "../movies/pages/search/SearchPage";
import { MoviePage } from "../movies/pages/movie/MoviePage";


export const appRouter = createBrowserRouter([
    {
        path: '/',
        element: <MoviesLayout />,
        children: [{
            index: true,
            element: <HomePage />
        },
        {
            path: "/search",
            element: <SearchPage />
        },
        {
            path: "/movie",
            element: <MoviePage />
        },]
    }
])