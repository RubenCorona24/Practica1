let socket = new WebSocket('ws://localhost:8080')
let mensajeIngresado = document.getElementById("mensaje");
let boton = document.getElementById("boton");

//función para mostrar los mensajes en el contenedor
function mostrarMensajes(contenido){
    let contenedor = document.getElementById("mensajesChat");
    let elementoMensaje = document.createElement("p")
    elementoMensaje.textContent = contenido
    contenedor.appendChild(elementoMensaje)
}
boton.addEventListener("click",function(){
    let mensaje = mensajeIngresado.value;
    mostrarMensajes(mensaje)
    socket.send(mensaje)
});

socket.onmessage = function(event){
    let mensaje = event.data;
    mostrarMensajes(mensaje);
}