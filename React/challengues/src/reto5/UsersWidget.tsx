import { useGetUsers } from "./hooks/useGetUsers"
import { UsersGridCard } from "./UsersGridCard"
import { Input } from "../components/ui/input"

import { useState } from "react"

import { Badge } from '../components/ui/badge'

import { Link } from "react-router"
import { Button } from "../components/ui/button"


export const UsersWidget = () => {


    const [search, setsearch] = useState('')
    //TODO: Implementar Practicas: useEffect, async/await, peticiones HTTP y estados de carga.
    //consumir el useGetUsers
    const { data: users = [], isLoading, isError } = useGetUsers()
    if (isLoading) {
        return (
            <div className="flex min-h-[50vh] flex-col items-center justify-center gap-3 text-muted-foreground">
                <span className="h-8 w-8 animate-spin rounded-full border-2 border-primary/30 border-t-primary" />
                <p className="text-sm">Cargando usuarios...</p>
            </div>
        )
    }
    if (isError) {
        return (
            <div className="mx-auto mt-12 max-w-md rounded-2xl border border-destructive/30 bg-destructive/10 p-6 text-center text-sm font-medium text-destructive">
                Error al cargar usuarios
            </div>
        )
    }
    const query = search.toLowerCase().trim()
    const filteredUsers = users.filter(user => user.username.toLowerCase().includes(query)
        || user.name.toLowerCase().includes(query))

    return (
        <div className="container mx-auto max-w-7xl px-4 py-10">
            {/* Encabezado */}
            <div className="flex flex-col gap-6 sm:flex-row sm:items-end sm:justify-between">
                <div>
                    <span className="inline-flex items-center gap-2 rounded-full border border-border/60 bg-muted/50 px-3 py-1 text-xs font-medium text-muted-foreground">
                        <span className="h-1.5 w-1.5 animate-pulse rounded-full bg-primary" />
                        Directorio
                    </span>
                    <h1 className=" mt-3 text-3xl font-bold tracking-tight sm:text-4xl">Company Users</h1>
                    <p className="mt-1 text-sm text-muted-foreground">
                        {users.length} usuarios registrados
                    </p>
                </div>
                <Link to={"/users/new"}>
                    <Button className={"cursor-pointer rounded-xl px-5 shadow-sm transition-all hover:-translate-y-0.5 hover:shadow-md"}>
                        + Agregar Nuevo Usuario
                    </Button>
                </Link>
            </div>

            {/* Buscador */}
            <div className="relative mt-8">
                <svg className="pointer-events-none absolute left-4 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground" fill="none" stroke="currentColor" strokeWidth={2} viewBox="0 0 24 24">
                    <circle cx="11" cy="11" r="7" />
                    <path d="m20 20-3.5-3.5" strokeLinecap="round" />
                </svg>
                <Input placeholder="Nombre de Usuario"
                    type="text"
                    className="h-12 rounded-xl border-border/60 bg-card pl-11 shadow-sm transition-all focus-visible:ring-2 focus-visible:ring-primary/30"
                    onChange={(e) => setsearch(e.target.value)} />
            </div>

            <div className="mt-6">
                {
                    filteredUsers.length === 0 ? (
                        <div className="flex flex-col items-center justify-center gap-3 rounded-2xl border border-dashed border-border py-16 text-center">
                            <Badge variant="destructive" className="rounded-full px-3">Sin usuarios</Badge>
                            <p className="text-sm text-muted-foreground">Prueba con otro nombre de búsqueda.</p>
                        </div>) : <UsersGridCard users={filteredUsers} />
                }
            </div>


        </div>

    )
}
