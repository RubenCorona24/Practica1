import { AdminLayout } from "@/admin/layout/AdminLayout";
import { AdminPage } from "@/admin/pages/AdminPage";
import { HeroesLayout } from "@/heroes/layouts/HeroesLayout";
import { SuperheroProfile } from "@/heroes/pages/hero/HeroPage";
import { HomePage } from "@/heroes/pages/home/HomePage";
import { lazy } from "react";
import { createHashRouter } from "react-router";

const SearchPage = lazy(() => import("@/heroes/pages/search/SearchPage"))
//export const appRouter = createBrowserRouter([
export const appRouter = createHashRouter([
    {
        path: '/',
        element: <HeroesLayout />,
        children: [{
            index: true,
            element: <HomePage />
        },
        {
            path: "/heroes/:idSlug",
            element: <SuperheroProfile />
        },
        {
            path: "/search",
            element: <SearchPage />
        }, {
            path: '*',
            element: <HomePage />
        }]
    },
    {
        path: '/admin',
        element: <AdminLayout />,
        children: [
            {
                path: "/admin",
                element: <AdminPage />
            }
        ]
    }
])