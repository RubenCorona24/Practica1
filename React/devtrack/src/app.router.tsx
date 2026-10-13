import { createBrowserRouter } from 'react-router'
import { Dashboard } from './pages/dashboard/DashboardPage'
import { Layout } from './layout/Layout'
import { NotFoundPage } from './pages/notfound/NotFoundPage'

export const appRouter = createBrowserRouter([
    //Public Routes
    {
        path: '/',
        element: <Layout />,
        children: [
            {
                index: true,
                element: <Dashboard />
            }
        ]
    },
    {
        path: '*',
        element: <NotFoundPage />
    }
])