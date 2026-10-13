import { RouterProvider } from "react-router"
import { appRouter } from "./app.router"

export const DevTrackApp = () => {
    return (
        <RouterProvider router={appRouter} /> //pages router
    )
}
