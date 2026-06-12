//2DA Parte de prueba de API con colección estudiantes

//configurar conexión con la base de datos
const express = require("express");
const {MongoClient} = require("mongodb");
const app = express();
app.use(express.json()) //configurar a formato json

const client = new MongoClient("mongodb://localhost:27017/mibase");
let colEstudiantes; //variable de colección de estudiantes

//Conectar al iniciar
async function conectar() {
    const conexion = await client.connect();
    colEstudiantes = conexion.db().collection("estudiantes")
    console.log("Conectado a MongoDB✅")
}

//-----ENDPOINTS-----

//GET de todos los estudiantes
app.get("/estudiantes",async(pedido,respuesta) => {
    try{
        let datos= await colEstudiantes.find().toArray()
        respuesta.json(datos)
    }catch(error){
        respuesta.status(500).json({error:error.message})
    }
})

//GET un empleado por nombre
app.get("/estudiantes/:nombre",async(pedido,respuesta) => {
    try{
        let nombre = pedido.params.nombre //leer parámetro de la URL
        let estudiante = await colEstudiantes.findOne({nombre:nombre})
        if(!estudiante){
            return respuesta.status(404).json({mensaje:"No encontrado"})
        }
        respuesta.json(estudiante) //enviamos info del estudiante
    }catch(error){
        respuesta.status(500).json({error:error.message})
    }
})

//POST: Agregar nuevo estudiante
app.post("/estudiantes",async(pedido,respuesta) => {
    try{
        let nuevoEstudiante = pedido.body //leer el body de la petición
        let resultado = await colEstudiantes.insertOne(nuevoEstudiante)
        respuesta.json({mensaje:"Estudiante agregado ✅"},resultado)
    }catch(error){
        respuesta.status(500).json({error:error.message})
    }
})

//DELETE: Eliminar estudiante

app.delete("/estudiantes/:nombre",async(pedido,respuesta) =>{
    try{
        let nombre = pedido.params.nombre //extraemos nombre de la URL
        let resultado = await colEstudiantes.deleteOne({nombre:nombre}) //filtramos
        respuesta.json({mensaje:"Estudiante eliminado ✅"},resultado)
    }catch(error){
        respuesta.status(500).json({error:error.message})
    }
})
//Llamamos a la función para conectarnos
conectar()
.then(() =>{
    app.listen(3000, ()=>{
        console.log("Servidor corriendo en puerto 3000 🚀")
    })
})