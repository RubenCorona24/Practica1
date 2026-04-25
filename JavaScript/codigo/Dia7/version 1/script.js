function extraerNumero(elemento){
    let miElemento = document.getElementById(elemento)
    let miTexto = miElemento.value;
    let miNumero = parseInt(miTexto)
    return miNumero //Retornamos el número
}
//creamos función calcular
function calcular(){
    let ventas1,ventas2,ventas3,ventas4,vetas5,ventas6; //variables ventas
    ventas1 = extraerNumero("ventasTienda1") 
    ventas2 = extraerNumero("ventasTienda2") 
    ventas3 = extraerNumero("ventasTienda3") 
    ventas4 = extraerNumero("ventasTienda4") 
    ventas5 = extraerNumero("ventasTienda5") 
    ventas6 = extraerNumero("ventasTienda6") 
    //hacemos suma
    let totalVentas = ventas1 + ventas2+ ventas3+ ventas4+ ventas5+ ventas6
    let mensajeSalida = "Total Ventas: "+totalVentas;
    let elementoSalida = document.getElementById("parrafoSalida")
    elementoSalida.textContent = mensajeSalida
}