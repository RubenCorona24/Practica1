//Importar plugins
const { getAge, getUUID } = require("../plugins")
//Factory function: Función que crea una función
const obj = { name: "john", birthdate: "2009-01-19" }

//Función buildPerson
const buildPerson = ({ name, birthdate }) => { //recibe name y birthdate 
    return {
        id: getUUID(),
        name,
        birthdate,
        age: getAge(birthdate)
    }
}
//creamos el objeto con la función buildPerson
//const john = buildPerson(obj)
//
console.log(john)

module.exports = {
    buildPerson
}