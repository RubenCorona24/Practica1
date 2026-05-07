//función de agregar tarjeta
function agregarTarjeta(){
    //extraer elementos
    let color = document.getElementById("color")
    let contenedor = document.getElementById("contenedor")
    //agregar elementos div
    let parrafo = document.createElement("p")
    parrafo.textContent = "Este es un párrafo agregado"
    parrafo.style.color = color
    //agregar párrafo al contedor
    contenedor.appendChild(parrafo)
    
}

//función de eliminar párrafos
function eliminarParrafos(){
    let contenedor = document.getElementById("contenedor")
    contenedor.innerHTML = ""
}