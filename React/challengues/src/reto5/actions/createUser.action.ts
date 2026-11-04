import type { UserFormInformation } from "../interfaces/interface";
import type { User } from "../interfaces/interface";


export const createUserAction = async (newUser: UserFormInformation): Promise<User> => {
    const res = await fetch("https://jsonplaceholder.typicode.com/users", {
        method: 'POST',
        body: JSON.stringify(newUser),
        headers: {
            'Content-type': 'application/json; charset=UTF-8'
        }
    })
    if (!res.ok) throw new Error(`Error al crear usuario: ${res.status}`)
    const data = await res.json()
    return {
        id: data.id,
        name: data.name,
        username: data.username,
        email: data.email,
        phone: data.phone,
        website: data.website,
        address: { street: "", suite: "", city: data.city, zipcode: "", geo: { lat: "0", lng: "0" } },
        company: { name: "", catchPhrase: "", bs: "" },
    }
}