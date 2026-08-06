import { useMovie } from "@/movies/hooks/useMovie";
import { Clapperboard, Clock, Star, Users, Award, DollarSign, Globe } from "lucide-react";
import { Link, useParams } from "react-router";




// Utilidad: convierte "a, b, c" en lista y oculta valores "N/A"
const toList = (value: string) =>
    value === "N/A" ? [] : value.split(",").map((item) => item.trim());
const show = (value: string) => (value === "N/A" ? "Sin datos" : value);

// ---------- 5. Componente principal de la ficha ----------
export const MoviePage = () => {
    const { id = '' } = useParams() //extraemos el id del URL
    const { data: movie, isLoading, isError } = useMovie(id)
    if (isLoading) return <p>Loading...</p>
    if (isError) return <p>Error al extraer datos de película</p>
    if (!movie) return null
    console.log('movie recibido:', movie)
    const genres = toList(movie?.Genre);
    const actors = toList(movie?.Actors);

    return (
        <div className="min-h-screen bg-background">
            {/* ---------- 6. Barra de navegación fija ---------- */}
            <header className="sticky top-0 z-50 border-b border-border/60 bg-background/80 backdrop-blur-xl">
                <nav className="mx-auto flex max-w-6xl items-center justify-between px-5 py-4">
                    <Link to="/" className="flex items-center gap-2">
                        <Clapperboard className="size-6 text-primary" />
                        <span className="font-display text-2xl tracking-[0.12em] text-foreground">
                            CINEVERSO
                        </span>
                    </Link>
                    <span className="rounded-full bg-secondary px-4 py-2 text-sm text-foreground">
                        Ficha de película
                    </span>
                </nav>
            </header>

            {/* ---------- 7. Cabecera con póster de fondo ---------- */}
            <section className="relative overflow-hidden">
                <img
                    src={movie.Poster}
                    alt=""
                    aria-hidden="true"
                    className="absolute inset-0 size-full scale-110 object-cover opacity-25 blur-2xl"
                />
                <div className="absolute inset-0 bg-gradient-to-b from-background/40 via-background/80 to-background" />

                <div className="relative mx-auto grid max-w-6xl gap-8 px-5 py-12 md:grid-cols-[280px_1fr] md:py-16">
                    {/* 7.1 Póster principal */}
                    <img
                        src={movie.Poster}
                        alt={`Póster de ${movie.Title}`}
                        className="w-full max-w-[280px] rounded-xl border border-border/60 shadow-2xl"
                        loading="eager"
                    />

                    {/* 7.2 Título, metadatos y sinopsis */}
                    <div>
                        <h1 className="font-display text-5xl leading-none tracking-[0.04em] text-foreground md:text-6xl">
                            {movie.Title}
                        </h1>

                        <div className="mt-4 flex flex-wrap items-center gap-3 text-sm text-muted-foreground">
                            <span>{movie.Year}</span>
                            <span className="rounded border border-border px-2 py-0.5">{movie.Rated}</span>
                            <span className="flex items-center gap-1">
                                <Clock className="size-4" />
                                {movie.Runtime}
                            </span>
                            <span className="flex items-center gap-1 text-foreground">
                                <Star className="size-4 fill-primary text-primary" />
                                {movie.imdbRating}
                                <span className="text-muted-foreground">({movie.imdbVotes} votos)</span>
                            </span>
                        </div>

                        {/* 7.3 Géneros */}
                        <div className="mt-4 flex flex-wrap gap-2">
                            {genres.map((genre) => (
                                <span
                                    key={genre}
                                    className="rounded-full bg-secondary px-3 py-1 text-xs text-foreground"
                                >
                                    {genre}
                                </span>
                            ))}
                        </div>

                        <p className="mt-6 max-w-2xl text-base leading-relaxed text-muted-foreground">
                            {movie.Plot}
                        </p>

                        {/* 7.4 Reparto */}
                        <div className="mt-6">
                            <h2 className="flex items-center gap-2 text-sm font-semibold text-foreground">
                                <Users className="size-4 text-primary" />
                                Reparto principal
                            </h2>
                            <div className="mt-2 flex flex-wrap gap-2">
                                {actors.map((actor) => (
                                    <span
                                        key={actor}
                                        className="rounded-lg border border-border/60 px-3 py-1.5 text-sm text-muted-foreground"
                                    >
                                        {actor}
                                    </span>
                                ))}
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            {/* ---------- 8. Calificaciones por fuente ---------- */}
            <section className="mx-auto max-w-6xl px-5 pb-4">
                <h2 className="font-display text-3xl tracking-[0.08em] text-foreground">
                    CALIFICACIONES
                </h2>
                <div className="mt-4 grid gap-4 sm:grid-cols-3">
                    {movie.Ratings.map((rating) => (
                        <div
                            key={rating.Source}
                            className="rounded-xl border border-border/60 bg-card p-5"
                        >
                            <p className="text-xs uppercase tracking-wide text-muted-foreground">
                                {rating.Source}
                            </p>
                            <p className="mt-2 font-display text-4xl text-primary">{rating.Value}</p>
                        </div>
                    ))}
                </div>
            </section>

            {/* ---------- 9. Ficha técnica ---------- */}
            <section className="mx-auto max-w-6xl px-5 py-10">
                <h2 className="font-display text-3xl tracking-[0.08em] text-foreground">
                    FICHA TÉCNICA
                </h2>
                <dl className="mt-4 grid gap-x-8 gap-y-4 sm:grid-cols-2 lg:grid-cols-3">
                    {[
                        { label: "Director", value: show(movie.Director) },
                        { label: "Guion", value: show(movie.Writer) },
                        { label: "Estreno", value: show(movie.Released) },
                        { label: "Idiomas", value: show(movie.Language) },
                        { label: "País", value: show(movie.Country) },
                        { label: "Metascore", value: show(movie.Metascore) },
                        { label: "Productora", value: show(movie.Production) },
                        { label: "ID IMDb", value: show(movie.imdbID) },
                        { label: "Tipo", value: show(movie.Type) },
                    ].map((item) => (
                        <div key={item.label} className="border-t border-border/60 pt-3">
                            <dt className="text-xs uppercase tracking-wide text-muted-foreground">
                                {item.label}
                            </dt>
                            <dd className="mt-1 text-sm text-foreground">{item.value}</dd>
                        </div>
                    ))}
                </dl>

                {/* 9.1 Premios y taquilla destacados */}
                <div className="mt-8 grid gap-4 sm:grid-cols-2">
                    <div className="flex items-start gap-3 rounded-xl border border-border/60 bg-card p-5">
                        <Award className="mt-0.5 size-5 shrink-0 text-primary" />
                        <div>
                            <p className="text-xs uppercase tracking-wide text-muted-foreground">
                                Premios
                            </p>
                            <p className="mt-1 text-sm text-foreground">{show(movie.Awards)}</p>
                        </div>
                    </div>
                    <div className="flex items-start gap-3 rounded-xl border border-border/60 bg-card p-5">
                        <DollarSign className="mt-0.5 size-5 shrink-0 text-primary" />
                        <div>
                            <p className="text-xs uppercase tracking-wide text-muted-foreground">
                                Taquilla
                            </p>
                            <p className="mt-1 text-sm text-foreground">{show(movie.BoxOffice)}</p>
                        </div>
                    </div>
                </div>

                {/* 9.2 Sitio oficial (si existe) */}
                {movie.Website !== "N/A" && (
                    <a
                        href={movie.Website}
                        className="mt-6 inline-flex items-center gap-2 text-sm text-primary hover:underline"
                    >
                        <Globe className="size-4" />
                        Sitio oficial
                    </a>
                )}
            </section>

            {/* ---------- 10. Pie de página ---------- */}
            <footer className="border-t border-border/60 py-8 text-center text-sm text-muted-foreground">
                <Link to="/" className="hover:text-foreground">
                    ← Volver a las recomendadas
                </Link>
            </footer>
        </div>
    );
}