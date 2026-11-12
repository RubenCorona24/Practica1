const getAgePlugin = require('get-age') //adaptar el paquete
const getAge = (birthdate) => {
    if (!birthdate) return new Error("birthdate is required")
    return getAgePlugin(birthdate) //retornamos la fecha extraída
}

module.exports = {
    getAge
}