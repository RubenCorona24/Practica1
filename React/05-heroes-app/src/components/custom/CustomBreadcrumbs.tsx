
import {
    Breadcrumb,
    BreadcrumbEllipsis,
    BreadcrumbItem,
    BreadcrumbLink,
    BreadcrumbList,
    BreadcrumbPage,
    BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"
import { Button } from "@/components/ui/button"
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuGroup,
    DropdownMenuItem,
    DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { Link } from "react-router";
interface Breadcrumb {
    label: string,
    to: string
}

interface Props {
    pageName: string,
    breadcrumbs: Breadcrumb[];
}
export const CustomBreadcrumbs = ({ pageName, breadcrumbs = [] }: Props) => {
    const [b1, b2, b3] = breadcrumbs
    return (
        <Breadcrumb>
            <BreadcrumbList>
                <BreadcrumbItem>
                    <BreadcrumbLink render={<a href="/">Home</a>} />
                </BreadcrumbItem>
                <BreadcrumbSeparator />
                <BreadcrumbItem>
                    <DropdownMenu>
                        <DropdownMenuTrigger render={<Button size="icon-sm" variant="ghost"><BreadcrumbEllipsis /><span className="sr-only">Toggle menu</span></Button>} />
                        <DropdownMenuContent align="start">
                            <DropdownMenuGroup>
                                <DropdownMenuItem>
                                    <Link to={`/${b1.to}`}>{b1.label}</Link>
                                </DropdownMenuItem>
                                <DropdownMenuItem>
                                    <Link to={`/${b2.to}`}>{b2.label}</Link>
                                </DropdownMenuItem>
                                <DropdownMenuItem>
                                    <Link to={`/${b3.to}`}>{b3.label}</Link>
                                </DropdownMenuItem>
                            </DropdownMenuGroup>
                        </DropdownMenuContent>
                    </DropdownMenu>
                </BreadcrumbItem>
                <BreadcrumbSeparator />
                <BreadcrumbItem>
                    <BreadcrumbLink className="text-black" render={<a href="#">{pageName}</a>} />
                </BreadcrumbItem>
                <BreadcrumbSeparator />
                <BreadcrumbItem>
                    <BreadcrumbPage>Breadcrumb</BreadcrumbPage>
                </BreadcrumbItem>
            </BreadcrumbList>
        </Breadcrumb>
    )
}
