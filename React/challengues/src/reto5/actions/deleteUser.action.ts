
export const deleteUserAction = async (id: number) => {
    const res = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`, {
        method: "DELETE"
    })
    if (!res.ok) throw new Error(`Error estatus ${res.status} al eliminar usuario`)
}   