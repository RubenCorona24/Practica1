
import { useNavigate, useParams } from 'react-router';

import { useProduct } from '@/admin/hooks/useProduct';
import { CustomFullScreenLoading } from '@/components/custom/CustomFullScreenLoading';
import { ProductForm } from './ui/ProductForm';

interface Product {
    id: string;
    title: string;
    price: number;
    description: string;
    slug: string;
    stock: number;
    sizes: string[];
    gender: string;
    tags: string[];
    images: string[];
}

export const AdminProductPage = () => {
    const { id } = useParams(); //extraer id de parámetros

    const navigate = useNavigate()
    const { isLoading, isError, data: product } = useProduct(id ?? '') //consumir customHook
    console.log({ isLoading, product })

    const title = id === 'new' ? 'Nuevo producto' : 'Editar producto';
    const subtitle =
        id === 'new'
            ? 'Aquí puedes crear un nuevo producto.'
            : 'Aquí puedes editar el producto.';


    //redirecciones
    if (isError) {
        navigate("/admin/products")
    }
    if (isLoading) return <CustomFullScreenLoading />
    if (!product) {
        navigate("/admin/products")
    }
    return <ProductForm title={title} subTitle={subtitle} product={product} />



};
