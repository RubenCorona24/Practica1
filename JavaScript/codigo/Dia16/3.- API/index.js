//APIS: GET Y POST

//importar el framework express
const express = require("express")
const app = express();

//obtener el modulo conexion.js
const mongoDB = require("./conexion") //llamo al archivo

//configurar nuestra API para trabajar bajo el formato JSON
app.use(express.json());


//Definir un nuevo método GET: seleccionar clientes
app.get("/clientes",(pedido,respuesta) =>{
    //Obtener listado de clientes
    mongoDB.conexionDB()
    .then((conexion) => {
        const controlador = conexion.db().collection("clientes");
        controlador.find().toArray()
            .then((filas) => respuesta.send(filas)) //enviamos las filas
            .catch((error) => respuesta.send(error));
    })
})

//Definir método POST
app.post("/clientes/create",(pedido,respuesta) => {
     mongoDB.conexionDB()
     .then((conexion) => {
        const controlador = conexion.db().collection("clientes");
        controlador.insertOne(pedido.body)
        .then(respuesta.send("Nuevo registro creado"))
        .catch((error) => respuesta.send(error))
     })
})

//Iniciar el servidor en el puerto 3000
app.listen(3000,()=>{
    console.log("El servidor está en línea")
}) //no. de puerto y callback
