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