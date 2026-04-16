let elementoPrecio = document.getElementById("precio")
let elementoDecision = document.getElementById("decision")
function evaluarCompra(){
    let precio = parseInt(elementoPrecio.value)
    //empezamos con la evaluación
    if (precio<= 20){
        elementoDecision.textContent = "Comprar 2 cartones de leche"
    } else{
        if (precio<=25){
            elementoDecision.textContent = "Comprar 1 carton de leche"

        } else {
            elementoDecision.textContent = "No comprar leche"
        }
    }
}