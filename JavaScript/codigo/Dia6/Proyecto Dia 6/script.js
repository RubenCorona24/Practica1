//array de 5 calificaciones
let calificaciones = [9,8,9,10,9]
let elementoLista = document.getElementById("listaCalificaciones")
let elementoPromedio = document.getElementById("promedio")
let elementoNotaAlta = document.getElementById("notaAlta")
let elementoAplazo = document.getElementById("aplazo")
// mostrar 4 botones
// mostrar lista con notas - funcion co ul y li - for of
function mostrarLista(){
    elementoLista.innerHTML = ""  // limpiar antes de mostrar
    for (let calificacion of calificaciones){
        let item = document.createElement("li")
        item.innerText = "Calificación: "+calificacion //texo
        elementoLista.appendChild(item) //agregamos el item
    }
}

//calcular promedio - loop for
function sacarPromedio(){
    let sumatoria = 0
    let contador = 0
    for (let calificacion of calificaciones){
        sumatoria = sumatoria + calificacion
        contador++
    }
    let promedio = sumatoria / contador
    elementoPromedio.textContent = "Promedio: "+promedio    
}
//obtener nota más alta - loop while
function obtenerNotaAlta(){
    let notaAlta = calificaciones[0] //asumimos que la primera es la más alta
    let i=1
    while(i<calificaciones.length){
        if (calificaciones[i] > notaAlta){
             notaAlta = calificaciones[i]  // si encontramos una mayor, la guardamos
        } i++
    }
    elementoNotaAlta.textContent = "Nota más alta: "+notaAlta
}
//establecer si hubo aplazos (calif. menor a 4) - loop do while
function establecerAplazos(){
    let i = 0 //inicializar en 0
    let huboAplazos = false //bandera para saber si hubo aplazos
    let mensajeAplazos = ""
    do {
        if (calificaciones[i] < 4) {
            huboAplazos = true
            mensajeAplazos += "❌ Aplazo en calificación " + (i + 1) + ": " + calificaciones[i] + " | "
        }
        i++
    } while (i < calificaciones.length)

    if (!huboAplazos) {
        elementoAplazo.textContent = "✅ No hubo aplazos"
    } else {
        elementoAplazo.textContent = mensajeAplazos  // ← mostrar todos juntos
    }
}
function reestablecer(){
    elementoLista.innerText = ""
    elementoPromedio.textContent = ""
    elementoNotaAlta.textContent = ""
    elementoAplazo.textContent = ""
}