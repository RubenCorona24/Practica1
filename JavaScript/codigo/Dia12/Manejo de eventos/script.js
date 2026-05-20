let boton = document.getElementById("miBoton")
let contenedor = document.getElementById("contenedor")
let enlace = document.getElementById("enlace")
function mostrarMensaje(event){
    alert(event.target);
    alert(event.currentTarget);
}

contenedor.addEventListener("click",mostrarMensaje)

//funcion de evitar acción por defecto (enlace)
function evitarEnlace(event){
    event.preventDefault();
    alert("Enlace no habilitado")
}
enlace.addEventListener("click",evitarEnlace) //agregamos escuchador de eventos