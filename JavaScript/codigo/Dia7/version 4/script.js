function crearParrafoTienda(numero, valorMin) {
    let elementoParrafo = document.createElement("p")

    // ✅ createElement en lugar de getElementById
    let elementoEtiqueta = document.createElement("label")
    elementoEtiqueta.innerText = "Tienda " + numero + ": "
    elementoEtiqueta.setAttribute("for", "ventasTienda" + numero)

    let elementoInput = document.createElement("input")
    elementoInput.setAttribute("type", "number")
    elementoInput.setAttribute("id", "ventasTienda" + numero)  // ✅ id consistente
    elementoInput.setAttribute("min", valorMin)
    elementoInput.setAttribute("value", 0)

    elementoParrafo.appendChild(elementoEtiqueta)
    elementoParrafo.appendChild(elementoInput)
    return elementoParrafo
}

function crearTiendas(contenedorID, min, cantidadTiendas) {
    let elementoContenido = document.getElementById(contenedorID)
    for (let conteoTiendas = 1; conteoTiendas <= cantidadTiendas; conteoTiendas++) {
        let parrafoTienda = crearParrafoTienda(conteoTiendas, min)  // ✅ pasar número
        elementoContenido.appendChild(parrafoTienda)
    }
}

function extraerNumero(elemento){
    let miTexto = elemento.value;
    let miNumero = parseInt(miTexto)
    return miNumero //Retornamos el número
}
function calcular(){
    let ventas = []
    let posicionVentas = 0;//inicializamos en 0
    let elementoVentas = document.getElementById("itemsTiendas") //extraemos elemento tiendas
    for (let item of elementoVentas.children){
        let valorVenta = extraerNumero(item.children[1]) 
        ventas[posicionVentas] = valorVenta
        posicionVentas = posicionVentas + 1
    }
    //hacemos suma
    let totalVentas = sumarTotal(vantas)
    let ventaMayor = sacarMayor(ventas)
    let ventaMenor = sacarMenor(ventas)
    let mensajeSalida = "Total Ventas: "+totalVentas +
        " / Venta Mayor: "+ventaMayor+
        " / Venta Menor: "+ventaMenor
    let elementoSalida = document.getElementById("parrafoSalida")
    elementoSalida.textContent = mensajeSalida
}
//función de sumar (obtener total)
function sumarTotal(array) {
    let total = 0;
    for (let venta of array){
        total = total+venta; //vamos sumando
    }
    return total;
}   

function sacarMayor(array){
    let maximo = array[0]
    for(let venta of array){
        if (venta>maximo){
            maximo = venta; //se reescribe la venta mayor
        }
    }
    return maximo
}

function sacarMenor(array){
    let menor = array[0]
    for(let venta of array){
        if (venta<menor){
            menor = venta; //se reescribe la venta mayor
        }
    }
    return menor
}