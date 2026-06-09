async function modificarDatos(){
    try{
        let respuesta = await fetch("https://jsonplaceholder.typicode.com/posts/4",{
            method:"PUT", //metodo put
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                title: "Nuevo título",
                body: "Nueva descripción"
            })
        })
        if(!respuesta.ok){ //valor booleano
            throw new Error("Error en la solicitud: "+respuesta.statusText);
        }
        let datos = await respuesta.json(); //parcheamos a formato json
        console.log(datos) //imprimimos datos modificados
    }catch(error){
        console.log("Error: "+error)
    }
}


//fetch para eliminar datos
async function eliminarDatos() {
    try{
        let respuesta = await fetch("https://jsonplaceholder.typicode.com/posts/4",{
            method: "DELETE",
        })
        if(!respuesta.ok){ //valor booleano
            throw new Error("Error en la solicitud: "+respuesta.statusText);
        }
        let datos = await respuesta.json();
        console.log("Datos eliminados: ",datos) //imprimimos datos eliminados 
    }catch(error){
        console.log("Error: "+error)
    }
}

async function modificarMinimamenteDatos() {
    try{
        let respuesta = await fetch("https://jsonplaceholder.typicode.com/posts/8",{
            method: "PATCH",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                title: "Nuevo título" //solo modificamos título
            })
        })
        if(!respuesta.ok){ //valor booleano
            throw new Error("Error en la solicitud: "+respuesta.statusText);
        }
        let datos = await respuesta.json();
        console.log("Body modificado: ",datos) //imprimimos datos eliminados 
    }catch(error){
        console.log("Error: "+error)
    }
}
modificarMinimamenteDatos()