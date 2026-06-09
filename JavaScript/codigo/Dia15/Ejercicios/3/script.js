let inputID = document.getElementById("idPost")
let btnBuscar = document.getElementById("btnBuscar")
let titulo = document.getElementById("tituloSpan")
let contenido = document.getElementById("contenidoSpan")
let btnComentarios = document.getElementById("btnComentarios")
let listaComentarios = document.getElementById("listaComentarios")
let btnPublicar = document.getElementById("btnPublicar")

btnBuscar.addEventListener("click",async function(){
    try{
        let id = inputID.value;
    let res = await fetch("https://jsonplaceholder.typicode.com/posts/"+id)
    if (!res.ok){
        throw new Error("Error")
    }
    let datos = await res.json()
    titulo.textContent = datos.title
    contenido.textContent = datos.body

    } catch(error){
        alert("Error: "+error)
    }
})

btnComentarios.addEventListener("click",async function () {
    listaComentarios.innerHTML = ""
    try{
        let id = inputID.value;
    let res = await fetch("https://jsonplaceholder.typicode.com/posts/"+id+"/comments")
    if (!res.ok){
        throw new Error("Error")
    }
    let datos = await res.json()
    for (let comentario of datos){
        let li = document.createElement("li")
        li.textContent = "Usuario: "+comentario.name + " Contenido: "+comentario.body
        listaComentarios.appendChild(li)
    }

    } catch(error){
        alert("Error: "+error)
    }
})

//agregar comentarios nuevo con POST
async function agregarPost(contenido,nombre) {
    try{
        let id = inputID.value;
        let res = await fetch("https://jsonplaceholder.typicode.com/posts/"+id+"/comments",{
            method: "POST",
            headers: {
                "Content-Type":"application/json"
            },
            body: JSON.stringify({
                postId:2,
                name:nombre,
                body:contenido
            })
        })
    if (!res.ok){
        throw new Error("Error")
    }
    let data = res.json();
    console.log("Usuario: "+nombre+"\n"+"Comentario: "+contenido)
    alert("Comentario Publicado")
    

    } catch(error){
        alert("Error: "+error)
    }
}
let contenedor = document.getElementById("contenedor")
    let label = document.createElement("label")
    label.setAttribute("for","usuario")
    label.textContent = "Nombre de Usuario: "
    let usuario = document.createElement("input")
    usuario.setAttribute("id","usuario")
    usuario.setAttribute("type","text")
    let label2 = document.createElement("label")
    label2.setAttribute("for","contenido")
    label2.textContent = "Comentario: "
    let comentario = document.createElement("input")
    comentario.setAttribute("id","contenido")
    comentario.setAttribute("type","text")
    contenedor.appendChild(label)
    contenedor.appendChild(usuario)
    contenedor.appendChild(label2)
    contenedor.appendChild(comentario)
btnPublicar.addEventListener("click",agregarPost(comentario.value,usuario.value))