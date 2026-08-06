import { Input } from '@base-ui/react'
import { Search, X } from 'lucide-react'
import { useRef, useState } from 'react'
import { useSearchParams } from 'react-router'

export const SearchControl = () => {
    const inputRef = useRef<HTMLInputElement>(null)  //referencia al input
    const [searchParams, setSearchParams] = useSearchParams()
    // 5.1 Estado de los filtros
    const [query, setQuery] = useState("");
    const setQueryParams = (query: string, value: string) => {
        setSearchParams(prev => {
            prev.set(query, value)
            return prev
        })
    }
    const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
        console.log(e.key)
        if (e.key === "Enter") { //verificar que la key sea Enter
            const valueInput = inputRef.current?.value ?? '' //extraemos valor de input
            setQueryParams("query", valueInput)
        }
    }
    return (
        <div className="relative mt-8 max-w-xl">
            <Search className="pointer-events-none absolute left-4 top-1/2 size-5 -translate-y-1/2 text-muted-foreground" />
            <Input
                ref={inputRef}
                type="text"
                defaultValue={searchParams.get("query") ?? ''}
                maxLength={100}
                onKeyDown={handleKeyDown}
                placeholder="Título, género o año..."
                aria-label="Buscar películas"
                className="w-full rounded-full border border-border bg-card py-4 pl-12 pr-11 text-sm text-foreground outline-none transition-colors placeholder:text-muted-foreground focus:border-primary"
            />
            {query !== "" && (
                <button
                    type="button"
                    onClick={() => setQuery("")}
                    aria-label="Limpiar búsqueda"
                    className="absolute right-3 top-1/2 -translate-y-1/2 rounded-full p-1.5 text-muted-foreground transition-colors hover:text-foreground"
                >
                    <X className="size-4" />
                </button>
            )}
        </div>

    )
}
