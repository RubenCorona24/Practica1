import {
    NavigationMenu,
    NavigationMenuItem,
    NavigationMenuLink,
    NavigationMenuList,
    // ...los que necesites
} from "@/components/ui/navigation-menu"
import { Link } from "react-router"

//TODO: Realizar el Custommenu
export const CustomMenu = () => {
    return (
        <NavigationMenu>
            <NavigationMenuList>
                <NavigationMenuItem>
                    <NavigationMenuLink
                        render={<Link to="/" />}
                        className={'bg-slate-200 rounded-md p-2'}
                    >
                        Inicio
                    </NavigationMenuLink>
                </NavigationMenuItem>
                <NavigationMenuItem>
                    <NavigationMenuLink
                        render={<Link to="/search" />}
                        className={'bg-slate-200 rounded-md p-2'}
                    >
                        Buscar
                    </NavigationMenuLink>
                </NavigationMenuItem>
            </NavigationMenuList>
        </NavigationMenu>
    )
}
