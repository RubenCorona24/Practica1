//Conexión con la base de datos MySQL
const express = require("express")
const app = express();
const mySQL = require("./conexion");
 
app.use(express.json())

//Métodos solicitados

//Método get de todos los estudiantes
app.get("/estudiantes", (request, response) => {
    mySQL.connection.query("SELECT * FROM estudiantes", function(error, filas) {
      if (error){
        return response.status(500).json({error:error.message})
      }
      response.json(filas); //enviamos las filas
    });
})

//Método get por legajo de estudiante
app.get("/estudiantes/:legajo", (request, response) => {
    let legajoEstudiante = request.params.legajo //extraemos legajo
    mySQL.connection.query("SELECT * FROM estudiantes WHERE legajo = ?", [legajoEstudiante], function(error, filas) {
      if (error){
        return response.status(500).json({error:error.message})
      }
      response.json(filas[0]); //enviamos las filas
    });
})

//Método POST de estudiantes
app.post("/estudiantes/create", (request, response) => {
    let {legajo,nombre,email} = request.body //extraemos datos del body
    mySQL.connection.query("INSERT INTO estudiantes (legajo,nombre,email) VALUES (?,?,?)",[legajo,nombre,email], function(error, results) {
      if (error){
        return response.status(500).json({error:error.message})
      }
      response.json({"mensaje":"Estudiante creado",id: results.insertId }); 
    });
})

//Método PUT pra modificar registro de tabla de exámenes por id de examen
app.put("/notas/:id",(request,response) => {
    let idNota = request.params.id
    let {legajo_estudiante,codigo_curso,nota,fecha} = request.body
    let query = "UPDATE notas SET legajo_estudiante = ?,codigo_curso=?,nota=?,fecha=? WHERE id = ?"
    mySQL.connection.query(query,[legajo_estudiante,codigo_curso,nota,fecha,idNota],(error,results) => {
        if(error){
            return response.status(500).json({error:error.message})
        }
        if (results.affectedRows === 0) {
        return response.status(404).json({ mensaje: "No encontrado" })
    }
        response.json({mensaje:"Nota actualizada"})
    })
})

//Método DELETE para eliminar un registro de nota segun id

app.delete("/notas/:id/delete",(request,response) => {
    let idNota = request.params.id;
    let query = "DELETE FROM notas WHERE id = ?"
    mySQL.connection.query(query,[idNota],(error,results) =>{
        if(error){
            return response.status(500).json({error:error.message})
        }
        response.json({mensaje:"Nota eliminada"})
    })
})

//Obtener notas de acuerdo al código de curso: SOLO los aprobados
app.get("/notas/:codigo_curso/aprobados",(request,response) => {
    let codigoCurso = request.params.codigo_curso;
    let query = "SELECT * FROM notas WHERE codigo_curso = ? AND nota >= 6"
    mySQL.connection.query(query,[codigoCurso],(error,filas) => {
        if(error){
            return response.status(500).json({error:error.message})
        }
        response.json(filas)
    })
})

app.listen(3000,() =>{
    console.log("Servidor en puerto 3000🚀")
})