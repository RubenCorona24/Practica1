//conexión a la base de datos
const {MongoClient} = require("mongodb")
const client = new MongoClient("mongodb://127.0.0.1:27017/mibase");

//Desarrollar una función para conectarnos con la base y retornar el objeto que contiene la conexión
const conexionDB = () => {
    return client.connect()
    .then((dbClient) =>{
        return dbClient;
    })
    .catch((error) =>{
        return error;
    })
    
}

//exportar el módulo 
module.exports = {conexionDB}