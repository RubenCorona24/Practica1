//configurar con ExpressJS el servidor de la app
const express = require("express");
const app = express();

app.set('port',3000);
app.listen(3000)

//Llamar al componente de mysql
var mysql = require("mysql2");

//establecer los parámetros de la conexión
var connection = mysql.createConnection({
    host:"localhost",
    user:"root",
    password: "C0RONA2026",
    database: "mibasenueva"
}) //pasamos el host,user,password,database

//ejecutar funciones CRUD

//Nos conectamos con la base
connection.connect(); 

//Agregar un nuevo registro
connection.query('INSERT INTO cliente VALUES (2,"Sebastian",1,12336,"AV. Siempreviva 4269")',function(error,resultados){
    if (error) throw error;
    console.log(resultados)
})

//Realizar la consulta a la tabla
connection.query('SELECT * FROM cliente',function(error,filas){
    if (error) throw error;
    console.log(filas)
})

//Realizar modificación de registro
connection.query('UPDATE cliente SET nombre = "Gerardo",telefono = 1227844 WHERE idCliente = 2',function(error,resultados){
    if(error) throw error;
    console.log(resultados)
})
connection.query('SELECT * FROM cliente',function(error,filas){
    if (error) throw error;
    console.log(filas)
})

//eliminar un registro
connection.query("DELETE FROM cliente WHERE idCliente = 2",function(error,resultados){
    if(error) throw error;
    console.log(resultados)
})
connection.query('SELECT * FROM cliente',function(error,filas){
    if (error) throw error;
    console.log(filas)
})
//cerramos la conexión
connection.end();