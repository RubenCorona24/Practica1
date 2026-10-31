
import {
    createBrowserRouter,
} from "react-router";
import { UsersWidget } from "../UsersWidget";

import { UserDetailPage } from "../UserDetailPage";


export const router = createBrowserRouter([
    {
        path: "/",
        element: <UsersWidget />
    },
    {
        path: "/users/:id",
        element: <UserDetailPage />
    },
    {
        path: "*",
        element: <UsersWidget />
    }
])