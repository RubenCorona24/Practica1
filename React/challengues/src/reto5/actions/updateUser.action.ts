import type { UserFormInformation } from "../interfaces/interface"
import type { User } from "../UserCard"

export const updateUserAction = async (id: number, data: UserFormInformation): Promise<User> => {
    const res = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`, {
        method: 'PUT',
        body: JSON.stringify(data),
        headers: { "Content-Type": "application/json; charset=UTF-8" }
    })
    if (!res.ok) throw new Error(`Error estatus ${res.status} al actualizar usuario`)
    const result: UserFormInformation & { id: number } = await res.json()
    return {
        id: result.id,
        name: result.name,
        username: result.username,
        email: result.email,
        phone: result.phone,
        website: result.website,
        address: { street: "", suite: "", city: result.city, zipcode: "", geo: { lat: "0", lng: "0" } },
        company: { name: "", catchPhrase: "", bs: "" },
    }
}