import { CustomHeader } from '../../../components/custom/CustomHeader'

import { Clapperboard, Star } from "lucide-react";
import heroBackdrop from "@/assets/hero-backdrop.jpg";
import poster1 from "@/assets/poster-1.jpg";
import poster2 from "@/assets/poster-2.jpg";
import poster3 from "@/assets/poster-3.jpg";
import poster4 from "@/assets/poster-4.jpg";
import poster5 from "@/assets/poster-5.jpg";
import poster6 from "@/assets/poster-6.jpg";
import type { Movie } from '../../interfaces/movie.interface';
import { MovieGridCard } from '../../components/MovieGridCard';
import { useQuery } from '@tanstack/react-query';
import { getMoviesAction } from '../../actions/get-movies.action';


const movies: Movie[] = [
    {
        id: "neon-horizonte",
        title: "Neón Horizonte",
        year: 2024,
        genres: ["Ciencia ficción", "Thriller"],
        rating: 8.7,
        duration: "2h 12m",
        synopsis:
            "En una ciudad que nunca apaga sus luces, un mensajero descubre que sus recuerdos fueron vendidos al mejor postor.",
        poster: poster1,
    },
    {
        id: "polvo-y-gasolina",
        title: "Polvo y Gasolina",
        year: 2023,
        genres: ["Acción", "Aventura"],
        rating: 8.1,
        duration: "1h 58m",
        synopsis:
            "Una corredora clandestina cruza el desierto en 48 horas para saldar una deuda imposible.",
        poster: poster2,
    },
    {
        id: "anillo-de-oro",
        title: "Anillo de Oro",
        year: 2025,
        genres: ["Ciencia ficción", "Drama"],
        rating: 9.0,
        duration: "2h 34m",
        synopsis:
            "La última tripulación humana orbita un planeta imposible buscando una señal que no debería existir.",
        poster: poster3,
    },
    {
        id: "lluvia-sobre-el-callejon",
        title: "Lluvia Sobre el Callejón",
        year: 2022,
        genres: ["Suspenso", "Noir"],
        rating: 7.9,
        duration: "1h 47m",
        synopsis:
            "Un detective retirado vuelve al caso que le costó todo, justo cuando la ciudad quiere olvidarlo.",
        poster: poster4,
    },
    {
        id: "el-bosque-que-respira",
        title: "El Bosque que Respira",
        year: 2024,
        genres: ["Terror", "Fantasía"],
        rating: 7.4,
        duration: "1h 39m",
        synopsis:
            "Cuatro amigos entran a un bosque donde la niebla recuerda el nombre de cada visitante.",
        poster: poster5,
    },
    {
        id: "ultimo-baile-en-la-azotea",
        title: "Último Baile en la Azotea",
        year: 2023,
        genres: ["Romance", "Drama"],
        rating: 8.3,
        duration: "2h 04m",
        synopsis:
            "Dos desconocidos se prometen un verano entero, sabiendo que solo les queda una noche.",
        poster: poster6,
    },
];

export const HomePage = () => {
    //extraer peliculas con useQuery
    const { data, isLoading, isError } = useQuery({
        queryKey: ['movies'],
        queryFn: getMoviesAction
    })
    const featured = movies[2]!;
    if (isLoading) return <p>Loading...</p>
    if (isError) return <p>Error al cargar películas</p>
    console.log({ data })
    return (
        <div className="min-h-screen bg-background">
            <header className="sticky top-0 z-50 border-b border-border/60 bg-background/80 backdrop-blur-xl">
                <nav className="mx-auto flex max-w-6xl items-center justify-between px-5 py-4">
                    <div className="flex items-center gap-2">
                        <Clapperboard className="size-6 text-primary" />
                        <span className="font-display text-2xl tracking-[0.12em] text-foreground">
                            CINEVERSO
                        </span>
                    </div>
                    <span className="rounded-full bg-secondary px-4 py-2 text-sm text-foreground">
                        Recomendadas
                    </span>
                </nav>
            </header>

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
                        Destacada: {featured.title} · {featured.rating.toFixed(1)}
                    </span>
                </div>

            </section>

            <main className="mx-auto max-w-6xl px-5 py-16">
                <h2 className="font-display text-4xl tracking-wide text-foreground">Recomendadas</h2>
                <MovieGridCard />
            </main>

            <footer className="border-t border-border/60 py-10 text-center text-xs uppercase tracking-[0.3em] text-muted-foreground">
                Cineverso
            </footer>
        </div>
    );
}
