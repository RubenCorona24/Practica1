import { Button } from "../components/ui/button"
import type { User } from './interfaces/interface'
import { Badge } from '../components/ui/badge'
import { Link, useNavigate } from 'react-router'
import { useDeleteUser } from "./hooks/useDeleteUser"

interface Props {
    users: User[]
}
export const UsersGridCard = ({ users }: Props) => {
    const navigate = useNavigate()
    const deleteUser = useDeleteUser()
    return (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-5 p-4">
            {users.map(user => (
                <div
                    key={user.id}
                    className="group relative flex flex-col overflow-hidden rounded-2xl border border-border/60 bg-card text-card-foreground shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-xl hover:border-primary/40"
                >
                    {/* Franja superior */}
                    <div className="h-20 bg-gradient-to-br from-primary/15 via-primary/5 to-transparent" />

                    {/* Avatar */}
                    <div className="-mt-12 flex justify-center">
                        <div className="rounded-full bg-card p-1 ring-1 ring-border/60 shadow-md">
                            <img
                                onClick={() => navigate(`/users/${user.id}`)}
                                src={`https://api.dicebear.com/9.x/initials/svg?seed=${user.name}`}
                                alt={user.username}
                                className="h-20 w-20 cursor-pointer rounded-full object-cover transition-transform duration-300 group-hover:scale-105"
                            />
                        </div>
                    </div>

                    <div className="flex flex-1 flex-col items-center gap-1 px-4 pb-4 pt-3 text-center">
                        <p className="w-full truncate text-base font-semibold tracking-tight">@{user.username}</p>
                        <p className="w-full truncate text-sm font-medium text-primary">{user.website}</p>
                        <Badge variant="secondary" className="mt-2 rounded-full px-3 font-normal">
                            {user.phone}
                        </Badge>

                        <div className="mt-auto w-full space-y-2 pt-4">
                            <Button
                                className="w-full cursor-pointer rounded-xl"
                                onClick={() => navigate(`/users/${user.id}`)}
                            >
                                Información
                            </Button>
                            <div className="grid grid-cols-2 gap-2">
                                <Link to={`/users/${user.id}/edit`}>
                                    <Button variant="outline" className="w-full cursor-pointer rounded-xl">
                                        Editar
                                    </Button>
                                </Link>
                                <Button
                                    variant="ghost"
                                    className="w-full cursor-pointer rounded-xl text-destructive hover:bg-destructive/10 hover:text-destructive"
                                    onClick={() => deleteUser.mutate(user.id)}
                                >
                                    Eliminar
                                </Button>
                            </div>
                        </div>
                    </div>
                </div>
            ))}
        </div>
    )
}