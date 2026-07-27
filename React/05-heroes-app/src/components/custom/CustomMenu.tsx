
import { Link } from 'react-router'
import { NavigationMenu, NavigationMenuItem, NavigationMenuLink, NavigationMenuList, navigationMenuTriggerStyle } from '../ui/navigation-menu'




export const CustomMenu = () => {
    return (
        <NavigationMenu>
            <NavigationMenuList>
                {/*Home */}
                <NavigationMenuItem>
                    <NavigationMenuLink
                        render={<Link to="/" />}
                        className={navigationMenuTriggerStyle()}
                    >
                        Inicio
                    </NavigationMenuLink>
                </NavigationMenuItem>

                {/*Search */}
                <NavigationMenuItem>
                    <NavigationMenuLink
                        render={<Link to="/search" />}
                        className={navigationMenuTriggerStyle()}
                    >
                        Buscar
                    </NavigationMenuLink>
                </NavigationMenuItem>
            </NavigationMenuList>

        </NavigationMenu>

    )
}
