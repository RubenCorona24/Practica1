//configurar conexión entre mysql y js con ExpressJS
const express = require("express");
const app = express();
app.set("port",3000);
app.listen(3000);
var mysql = require("mysql2")

//establecer los parámetros de la conexión
var connection = mysql.createConnection({
    host:"localhost",
    user:"root",
    password:"C0RONA2026",
    database:"proyectoproductos"
})

//conexión a la base
connection.connect(function(error){
    if(error){
        console.log(error);
        return;
    }
    console.log("Conexión exitosa!");
})

//realizamos consulta
connection.query('SELECT * FROM productos',function(error,filas){
    if(error) throw error;
    console.log(filas);
})

//finalizamos conexión
connection.end();