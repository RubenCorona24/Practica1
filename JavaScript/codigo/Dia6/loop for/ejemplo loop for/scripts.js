let elementoNumero = document.getElementById("elementoNumero")
function verTabla(){
    let numero = parseInt(elementoNumero.value)
    //obtener la tabla
    let elementoTabla = document.getElementById("listaTabla")
    elementoTabla.innerHTML = ""  // ← limpiar antes de generar
    //Producir y mostrar resultados
    for (let i=1;i<11;i++){
        //calcular el resultado
        let numResultado = numero * i;
        //Armar string con resultado
        let textoResultado = numero + " x " + i + " = "+ numResultado
        //crear un elemento de la lista
        let itemLista = document.createElement("li");
        itemLista.innerText = textoResultado
        elementoTabla.appendChild(itemLista)
    }
}