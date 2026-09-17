import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import { AdminTitle } from "../components/AdminTitle"
import { Link } from "react-router"
import { CustomPagination } from "@/components/custom/CustomPagination"
import { Button } from "@base-ui/react/button"
import { PlusIcon } from "lucide-react"

export const AdminProductsPage = () => {
    return (
        <>
            <div className="flex justify-between items-center">
                <AdminTitle title="Productos" description="Encuentra tus productos" />

                <div className="flex justify-end mb-10 gap-4">
                    <Link to={'/admin/products/new'}>
                        <Button>
                            <PlusIcon />
                            Nuevo Producto
                        </Button>
                    </Link>
                </div>

            </div>


            <Table className="bg-white p-10 shadow-xs border-gray 200 mb-10">
                <TableHeader>
                    <TableRow>
                        <TableHead className="w-[100px]">ID</TableHead>
                        <TableHead>Imagen</TableHead>
                        <TableHead>Nombre</TableHead>
                        <TableHead>Precio</TableHead>
                        <TableHead>Categoría</TableHead>
                        <TableHead>Stock</TableHead>
                        <TableHead>Tallas</TableHead>
                        <TableHead className="text-right">Acciones</TableHead>
                    </TableRow>
                </TableHeader>
                <TableBody>
                    <TableRow>
                        <TableCell className="font-medium">1</TableCell>
                        <TableCell>
                            <img src="https://placehold.co/250x250" alt="producto " className="w-20 h-20 object-cover rounded-md" />
                        </TableCell>
                        <TableCell>Producto</TableCell>
                        <TableCell>$250.00</TableCell>
                        <TableCell>Categoría 1</TableCell>
                        <TableCell>100 stock</TableCell>
                        <TableCell>XS, S, L</TableCell>
                        <TableCell className="text-right">
                            <Link to={"/admin/products/t-shirt-teslo"}>Editar</Link>
                        </TableCell>
                    </TableRow>
                </TableBody>
            </Table>

            <CustomPagination totalPages={5} />
        </>
    )
}
