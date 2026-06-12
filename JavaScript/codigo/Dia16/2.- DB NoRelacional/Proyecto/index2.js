//configurar con ExpressJS el servidor de la app
const express = require("express");
const app = express();

app.set('port',3000);
app.listen(3000)


const estudiantes = [
    {nombre:"Juan",carrera:"Informática",promedio:9,activo:true},
    {nombre:"Carlos",carrera:"Ingeniería en Software",promedio:10,activo:true},
    {nombre:"Jessy",carrera:"Ingenieria en Tecnologías Computacionales",promedio:10,activo:false},
    {nombre:"Robert",carrera:"Diseño",promedio:8,activo:true},
    {nombre:"Diana",carrera:"Gastronomía",promedio:9,activo:false}
]
//Llamar al objeto MongoClient del componente mongoDB
const {MongoClient} = require("mongodb")
const cliente = new MongoClient("mongodb://localhost:27017/mibase")
let res,filas;
async function usar(){
    try{
        const conexion = await cliente.connect();
        const colEstudiantes = conexion.db().collection("estudiantes") //nos conectamos a la colección de estudiantes

        //Consultas CRUD
        res = await colEstudiantes.insertMany(estudiantes) //insertamos estudiantes
        console.log("Insertados: ",res);

        //find() de estudiantes con buen promedio
        filas = await colEstudiantes.find({promedio: {$gte:8}}).toArray();
        console.log("Selección: ",filas);

        //updateOne modificar promedio de estudiante
        res = await colEstudiantes.updateOne({nombre:"Robert"},{$set: {promedio:9}});
        console.log("Promedio actualizado: ",res);

        //deleteOne eliminar un estudiante
        res = await colEstudiantes.deleteOne({nombre:"Diana"});
        console.log("Eliminado: ",res);

        //find de estudiantes solo activos
        filas = await colEstudiantes.find({activo:true}).toArray();
        console.log("Estudiantes activos: ",filas)

        
        
    }catch(error){
        console.log(error)
    }
}
usar();