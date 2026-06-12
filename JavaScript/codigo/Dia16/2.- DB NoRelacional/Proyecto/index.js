//configurar con ExpressJS el servidor de la app
const express = require("express");
const app = express();

app.set('port',3000);
app.listen(3000)



//Llamar al objeto MongoClient del componente mongoDB
const {MongoClient} = require("mongodb")
const cliente = new MongoClient("mongodb://localhost:27017/mibase")
let producto1 = {
    nombre:"IphoneXL",
    precio:500,
    stock:120,
    categoria:"Tecnología"
}
let producto2 = {
    nombre:"Samsung10",
    precio:300,
    stock:123,
    categoria:"Tecnología"
}
let producto3 = {
    nombre:"Camisa",
    precio:120,
    stock:300,
    categoria:"Ropa"
}
let producto4 = {
    nombre:"Lavadora",
    precio:400,
    stock:110,
    categoria:"Electrodomésticos"
}
let producto5 = {
    nombre:"Refrigerador",
    precio:900,
    stock:80,
    categoria:"Electrodomésticos"
}
let res,filas;
async function usar(){
    try{
        const conexion = await cliente.connect();
        const controlador = conexion.db().collection("prueba") //nos conectamos a la colección de prueba
        //insertMany de 5 productos
        res = await controlador.insertMany([producto1,producto2,producto3,producto4,producto5]);
        console.log("Insertado: ",res);

        //Realizar consulta find() de todos
        filas = await controlador.find().toArray(); //consultamos todo
        console.log("Filas: ",filas)

        //Búsqueda por filtro de categoría
        filas = await controlador.find({categoria: "Tecnología"}).toArray();
        console.log("Selección: ",filas);

        //Cambiar precio de un producto con updateOne
        res = await controlador.updateOne({nombre:"IphoneXL"},{$set: {precio:600}}); 
        console.log("Precio actualizado: ",res);

        //Eliminamos un producto
        res = await controlador.deleteOne({nombre:"Lavadora"});
        console.log("Producto eliminado: ",res);

        //Realizamos una consulta final de los productos
        filas = await controlador.find().toArray(); //consultamos todo
        console.log("Filas: ",filas)
    }catch(error){
        console.log(error)
    }
}
usar();