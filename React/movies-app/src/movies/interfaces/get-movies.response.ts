export interface MoviesResponse {
    Search: Search[];
    totalResults: string;
    Response: string;
}

export interface Search {
    Title: string;
    Year: string;
    imdbID: string;
    Type: pelicula;
    Poster: string;
}

export type pelicula =
    "movie" |
    "series"

