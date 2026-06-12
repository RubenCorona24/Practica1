//conexión a la base de datos de mongodb
const express = require("express");
const {MongoClient} = require("mongodb");
const app = express();

app.use(express.json());

const client = new MongoClient("mongodb://localhost:27017/mibase");
let colPrueba; //variable de colección de estudiantes

async function conectar(){
    const conexion = await client.connect();
    colPrueba = conexion.db().collection("prueba")
    console.log("Conectado a MongoDB✅")
}

//ENDPOINTS

//GET de todos los productos
app.get("/prueba",async(req,res) =>{
    try{
        let datos = await colPrueba.find().toArray(); 
        res.json(datos)
    }catch(error){
        res.status(500).json({error:error.message})
    }
})

//GET de un producto por nombre
app.get("/prueba/:nombre", async(req,res) => {
    try{
        let nombreProducto = req.params.nombre
        let producto = await colPrueba.findOne({nombre:nombreProducto})
        if(!producto){
            return respuesta.status(404).json({mensaje:"No encontrado"})
        }
        res.json(producto) //devolvemos producto
    }catch(error){
        res.status(500).json({error:error.message})
    }
})

//POST de un nuevo producto
app.post("/prueba",async(req,res) =>{
    try{
        let nuevoProducto = req.body //extraemos el body
        let resultado = await colPrueba.insertOne(nuevoProducto)
        res.json({mensaje:"Producto agregado ✅"},resultado)
    }catch(error){
        res.status(500).json({error:error.message})
    }
})

//UPDATE de un producto
app.put("/prueba/:nombre",async(req,res) =>{
    try{
        let nombreProducto = req.params.nombre
        let nuevosDatos = req.body
        let resultado = await colPrueba.updateOne({nombre:nombreProducto},{$set:nuevosDatos})
        res.json({ mensaje: "Producto modificado ✅", resultado })
    }catch(error){
        res.status(500).json({error:error.message})
    }
})

//DELETE de un producto
app.delete("/prueba/:nombre",async(req,res) =>{
    try{
        let nombreProducto = req.params.nombre
        let resultado = await colPrueba.deleteOne({nombre:nombreProducto})
        res.json({mensaje:"Producto eliminado✅"},resultado)
    }catch(error){
        res.status(500).json({error:error.message})
    }
})

//Llamamos a la función
conectar()
.then(() =>{
    app.listen(3000, () =>{
        console.log("Servidor corriendo en puerto 3000 🚀")
    })
})