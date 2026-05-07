//función de agregar a lista
function agregar(){
    //extraer elementos HTML
    let elementoProducto = document.getElementById("producto")
    let elementoLista = document.getElementById("listaProductos")
    //Crear elementos hijos en lista productos
    let producto = document.createElement("li")
    producto.textContent = elementoProducto.value //escribimos el nombre del producto
    //ponemos el elemento li en la lista
    elementoLista.appendChild(producto)

}

//función de limpiar lista
function limpiarLista(){
    let elementoLista = document.getElementById("listaProductos")
    //limpiamos lista con innetHTML
    elementoLista.innerHTML = ""
}