import { CustomHeader } from '@/components/custom/CustomHeader'
import { Outlet } from 'react-router'


export const Layout = () => {
    return (
        <div className="min-h-screen bg-background">
            <CustomHeader title='DevTrack App' subtitle='Crea y administra tus proyectos' />
            <Outlet />
        </div>
    )
}
