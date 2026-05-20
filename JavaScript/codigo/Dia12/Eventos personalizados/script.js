//extraemos elementos html
let audio = document.getElementById("audio")
let listaCanciones = document.getElementById("listaCanciones")

//añadimos escuchador de eventos a lista listaCanciones
listaCanciones.addEventListener("change",cambiarCancion)

function cambiarCancion(){
    let cancion = listaCanciones.value;
    audio.src = cancion
    audio.play();
    let evento = new CustomEvent("cambioDeCancion");
    audio.dispatchEvent(evento);
}
audio.addEventListener("cambioDeCancion",mostrarCancion);

function mostrarCancion(){
    console.log("La canción actual es; "+listaCanciones.value)
}

function agregarEvento() {
    let boton = document.getElementById('miBoton');

    boton.addEventListener('click', function() {
    let evento = new CustomEvent("evento");
    boton.dispatchEvent(evento)
    });
    boton.addEventListener("evento",function(){
        console.log("Boton presionado")
    })
}