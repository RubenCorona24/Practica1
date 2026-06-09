async function crearPost(titulo,contenido){ //usar función asíncrona
    try{
        let respuesta = await fetch("https://jsonplaceholder.typicode.com/posts",{
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                title: titulo,
                body: contenido,
                userId: 1
            }), //convierte objeto js en cadena json
        })
        if(!respuesta.ok){ //valor booleano
            throw new Error("Error en la solicitud: "+respuesta.statusText);
        }
        let data = await respuesta.json();
        console.log("Registro creado: ",data)
    }catch(error){
        alert(error)
    }
}

crearPost("Titulo de ejemplo","Contenido de ejemplo")