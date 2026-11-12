const users = [
    {
        id: 1,
        name: "John Doe"
    },
    {
        id: 2,
        name: "Jane Doe"
    }
]

//Función de flecha que extrae usuarios por id
const getUserById = (id, callback) => {
    const user = users.find(user => user.id === id) //devuelve true o false
    if (!user) return callback("User not found")

    return callback(null, user)
}

module.exports = {
    getUserById
}