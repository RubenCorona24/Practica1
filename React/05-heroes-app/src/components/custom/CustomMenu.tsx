
import { Link, useLocation } from 'react-router'
import { NavigationMenu, NavigationMenuItem, NavigationMenuLink, NavigationMenuList, navigationMenuTriggerStyle } from '../ui/navigation-menu'
import { cn } from '@/lib/utils'




export const CustomMenu = () => {
    const { pathname } = useLocation() //la ubicación actual del URL
    console.log({ pathname })

    const isActive = (path: string) => {
        return pathname === path
    }
    return (
        <NavigationMenu>
            <NavigationMenuList>
                {/*Home */}
                <NavigationMenuItem>
                    <NavigationMenuLink
                        render={<Link to="/" />}
                        className={cn(isActive('/') && 'bg-slate-200 rounded-md p-2')}
                    >
                        Inicio
                    </NavigationMenuLink>
                </NavigationMenuItem>

                {/*Search */}
                <NavigationMenuItem>
                    <NavigationMenuLink
                        render={<Link to="/search" />}
                        className={cn(isActive('/') && 'bg-slate-200 rounded-md p-2')}
                    >
                        Buscar
                    </NavigationMenuLink>
                </NavigationMenuItem>
            </NavigationMenuList>

        </NavigationMenu >

    )
}
