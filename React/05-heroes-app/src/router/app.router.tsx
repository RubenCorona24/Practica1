import { AdminLayout } from "@/admin/layout/AdminLayout";
import { AdminPage } from "@/admin/pages/AdminPage";
import { HeroesLayout } from "@/heroes/layouts/HeroesLayout";
import { HeroPages } from "@/heroes/pages/hero/HeroPages";
import { HomePage } from "@/heroes/pages/home/HomePage";
import { lazy } from "react";
import { createBrowserRouter } from "react-router";

const SearchPage = lazy(() => import("@/heroes/pages/search/SearchPage"))
export const appRouter = createBrowserRouter([
    {
        path: '/',
        element: <HeroesLayout />,
        children: [{
            index: true,
            element: <HomePage />
        },
        {
            path: "/heroes/:idSlug",
            element: <HeroPages />
        },
        {
            path: "/search",
            element: <SearchPage />
        }, {
            path: '*',
            element: <h1>Error 404</h1>
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