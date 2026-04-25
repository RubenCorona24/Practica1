//funcion de crear el item tienda (prototipo)
function crearParrafoTienda(textoLabel,valorMin){
    //crear las etiquetas de párrafo
    let elementoParrafo = document.createElement("p") //creamos elemento p
    //creaer etiqueta label
    let elementoEtiqueta = document.getElementById("label")
    elementoEtiqueta.innerText = textoLabel+ ": "
    //conectar con el input
    elementoEtiqueta.setAttribute("for",textoLabel)
    //crear el input
    let elementoInput = document.createElement("input")
    //establecer atributos de input
    elementoInput.setAttribute("type","number")
    elementoInput.setAttribute("id",textoLabel)
    elementoInput.setAttribute("min",valorMin)
    elementoInput.setAttribute("value",0)
    //agregar label e input al párrafo
    elementoParrafo.appendChild(elementoEtiqueta)
    elementoParrafo.appendChild(elementoInput)
    //devoler el parrafo completo
    return elementoParrafo
}

//funcion para crear tantos parrafos tienda como sea necesario
function crearTiendas(contenedorID,min,cantidadTiendas){
    //identificar el id del contenedor
    let elementoContenido = document.getElementById(contenedorID)
    //loop para crear tantas tiendas como se pidan
    for (let conteoTiendas=1;conteoTiendas<=cantidadTiendas;conteoTiendas++){
        //crear el texto de label para llamar a la funcion
        let textoLabel = "Tienda "+conteoTiendas 
        //crear tiendas con la función crearParrafoTienda
        let parrafoTienda = crearParrafoTienda(textoLabel,min);
        //agregar el parrafo al contenedor
        elementoContenido.appendChild(parrafoTienda) 
    }
}
function extraerNumero(elemento){
    let miElemento = document.getElementById(elemento)
    let miTexto = miElemento.value;
    let miNumero = parseInt(miTexto)
    return miNumero //Retornamos el número
}
function calcular(){
    let ventas = []
    ventas[0] = extraerNumero("ventasTienda1") 
    ventas[1] = extraerNumero("ventasTienda2") 
    ventas[2] = extraerNumero("ventasTienda3") 
    ventas[3] = extraerNumero("ventasTienda4") 
    ventas[4] = extraerNumero("ventasTienda5") 
    ventas[5] = extraerNumero("ventasTienda6") 
    //hacemos suma
    let totalVentas = sumarTotal(ventas)
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