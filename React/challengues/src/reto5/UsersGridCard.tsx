
import { Button } from "../components/ui/button"
import type { User } from './interfaces/interface'
import { Badge } from '../components/ui/badge'
import { useNavigate } from 'react-router'

interface Props {
    users: User[]
}
export const UsersGridCard = ({ users }: Props) => {
    const navigate = useNavigate()
    return (
        <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4 p-4">
            {users.map(user => (
                <div key={user.id} className="bg-white rounded-xl shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">
                    {/*Imagen controlada */}
                    <div className="flex justify-center pt-4">
                        <img
                            onClick={() => navigate(`/users/${user.id}`)}
                            src={`https://api.dicebear.com/9.x/initials/svg?seed=${user.name}`}
                            alt={user.username}
                            className='w-full h-full object-cover hover:scale-105 transition-transform duration-300' />

                    </div>
                    <div className='p-4'>
                        <p className='font-medium text-gray-800 truncate'>{user.username}</p>
                        <p className='text-blue-600 font-bold mt-1'>{user.website}</p>
                        <Button className='w-full mt-2 cursor-pointer'
                            onClick={() => navigate(`/users/${user.id}`)}>Información</Button>
                        <Badge>{user.phone}</Badge>
                    </div>
                </div>
            ))}
        </div>
    )
}
