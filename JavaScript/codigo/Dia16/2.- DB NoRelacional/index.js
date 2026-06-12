//configurar con ExpressJS el servidor de la app
const express = require("express");
const app = express();

app.set('port',3000);
app.listen(3000)

//Llamar al objeto MongoClient del componente mongoDB
const {MongoClient} = require("mongodb")

// Función asíncrona para hacer las peticiones al servidor
async function usar(){
    //crear nueva instancia de Mongo Client
    const client = new MongoClient("mongodb://localhost:27017/mibase");

    //nos conectamos y hacemos nuestras peticiones
    try{
        const conexion = await client.connect();
        const controlador = conexion.db().collection("clientes"); //llegamos a la colección clientes
        let respuesta,filas,filtro;

        //Insertar un nuevo registro
        const nuevoCliente = {nombre:"Ruben Santiago",genero:1,telefono:12234,domicilio:"Manzana 23"};
        respuesta = await controlador.insertOne(nuevoCliente) //insertamos nuevo cliente
        console.log("Insertado: ",respuesta);

        //Realizar una consulta
        filas = await controlador.find().toArray();
        console.log("Selección: ",filas);

        //modificar el registro anterior
        const cambiarCliente = {$set:{genero:1,telefono:12334343}};
        filtro = {nombre: "Ruben Santiago"} //usamos filtro
        respuesta = await controlador.updateOne(filtro,cambiarCliente);
        console.log("Actualizado: ",respuesta);
        
        //Realizar una consulta
        filtro = {genero:1} //usamos filtro de género
        filas = await controlador.find(filtro).toArray();
        console.log("Selección: ",filas)

        //eliminar un registro
        filtro = {nombre:"Ruben Santiago"};
        respuesta = await controlador.deleteOne(filtro);
        console.log("Eliminado: ",respuesta)

        //Realizamos una última consulta
        filas = await controlador.find().toArray();
        console.log("Selección: ",filas)
    }catch(error){
        console.log(error)
    }
}

usar(); //Llamamos a la función