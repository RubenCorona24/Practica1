import { useQuery } from '@tanstack/react-query';
import { CustomFooter } from '@/components/custom/CustomFooter';
import { CustomNavigationHeader } from '@/components/custom/CustomNavigationHeader';
import { SearchControl } from './UI/SearchControl';
import { MovieGrid } from '@/movies/components/MovieGrid';
import { useSearchParams } from 'react-router';
import { searchMoviesAction } from '@/movies/actions/search-movies.action';
import { toast } from "@/components/ui/toast"


// Lista única de géneros disponibles para los filtros

// ---------- 5. Componente principal de la página Buscar ----------
export const SearchPage = () => {
    const [searchParams] = useSearchParams()
    const query = searchParams.get("query") ?? '';
    const { data: movies, isLoading, isError } = useQuery({
        queryKey: ['movies', query],
        queryFn: () => searchMoviesAction(query),
        staleTime: 1000 * 60 * 5
    })

    if (isLoading) return <p>Loading...</p>
    if (isError) {
        toast.add({
            type: "warning",
            description: "Búsqueda no encontrada",
        })
        return <p>Error al cargar películas</p>
    }

    if (!movies) return null




    // 5.2 Filtrado en tiempo real (título, género o año)
    toast.add({
        type: "success",
        description: "Película encontrada.",
    })

    return (
        <div className="min-h-screen bg-background">
            {/* ---------- 6. Barra de navegación fija ---------- */}
            <CustomNavigationHeader title='Buscar' />

            {/* ---------- 7. Encabezado y buscador ---------- */}
            <section className="mx-auto max-w-6xl px-5 pt-14">
                <p className="text-xs uppercase tracking-[0.35em] text-accent">Catálogo completo</p>
                <h1 className="mt-3 font-display text-5xl tracking-wide text-foreground sm:text-7xl">
                    Buscar películas
                </h1>

                {/* 7.1 Campo de búsqueda */}
                <SearchControl />

            </section>

            <MovieGrid movies={movies} />

            {/* ---------- 9. Pie de página ---------- */}
            <CustomFooter />

        </div>
    );
}
