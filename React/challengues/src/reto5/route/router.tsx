
import {
    createBrowserRouter,
    Navigate,
} from "react-router";
import { UsersWidget } from "../UsersWidget";

import { UserDetailPage } from "../UserDetailPage";
import { UserFormPage } from "../UserFormPage";


export const router = createBrowserRouter([
    {
        path: "/",
        element: <UsersWidget />
    },
    {
        path: "/users/new",
        element: <UserFormPage />
    },
    {
        path: "/users/:id",
        element: <UserDetailPage />
    },
    {
        path: "/users/:id/edit",
        element: <UserFormPage />
    },
    {
        path: "*",
        element: <Navigate to="/" replace />
    }
])