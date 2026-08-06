import { CustomHeader } from '../../../components/custom/CustomHeader'

import { Star } from "lucide-react";
import heroBackdrop from "@/assets/hero-backdrop.jpg";
import { useQuery } from '@tanstack/react-query';
import { getMoviesAction } from '../../actions/get-movies.action';
import { CustomFooter } from '@/components/custom/CustomFooter';
import { CustomNavigationHeader } from '@/components/custom/CustomNavigationHeader';
import { MovieGrid } from '@/movies/components/MovieGrid';



export const HomePage = () => {
    //extraer peliculas con useQuery
    const { data, isLoading, isError } = useQuery({
        queryKey: ['movies'],
        queryFn: getMoviesAction
    })

    if (isLoading) return <p>Loading...</p>
    if (isError) return <p>Error al cargar películas</p>
    if (!data) return null
    console.log({ data })
    console.log('movies:', data)
    console.log('algún undefined?', data.some(m => m === undefined))
    return (
        <div className="min-h-screen bg-background">
            <CustomNavigationHeader title='Recomendadas ' />

            <section className="relative overflow-hidden">
                <img
                    src={heroBackdrop}
                    alt="Ciudad de neón bajo la lluvia"
                    width={1920}
                    height={1080}
                    className="absolute inset-0 h-full w-full object-cover opacity-40"
                />
                <div className="absolute inset-0 bg-[image:var(--gradient-hero)]" />
                <CustomHeader title="Encuentra la película que te va a desvelar" description='Una selección curada de historias que valen la noche.' />
                <div className="mt-8 flex flex-wrap items-center gap-3">
                    <span className="inline-flex items-center gap-2 rounded-full border border-border px-5 py-3 text-sm text-muted-foreground">
                        <Star className="size-4 fill-accent text-accent" />
                        Destacada: {/*featured.title*/} · {/*featured.rating.toFixed(1)*/}
                    </span>
                </div>

            </section>

            <main className="mx-auto max-w-6xl px-5 py-16">
                <h2 className="font-display text-4xl tracking-wide text-foreground">Recomendadas</h2>
                <MovieGrid movies={data} />
            </main>

            <CustomFooter />
        </div>
    );
}
