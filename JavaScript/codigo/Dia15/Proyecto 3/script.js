//cargar datos
let tabla = document.getElementById("tabla")
let libros = [] //array global
async function cargarDatos(){
    try{
        let res = await fetch("http://localhost:3000/libros")
        if (!res.ok){
            throw new Error("Error al extraer datos")
        }
        let datos = await res.json();
        libros = datos
        mostrarLibros() //llamamos a la función mostrar libros

    }catch(error){
        alert("Error: "+error)
    }
}

async function mostrarLibros(){
    tabla.innerHTML = ""
    for (let libro of libros){
        let tr = document.createElement("tr")
        let td = document.createElement("td")
        td.textContent = libro.id
        let td2 = document.createElement("td")
        td2.textContent = libro.titulo
        let td3 = document.createElement("td")
        td3.textContent = libro.autor
        let td4 = document.createElement("td")
        td4.textContent = libro.anio
        let td5 = document.createElement("td")
        td5.textContent = libro.disponible
        tr.appendChild(td)
        tr.appendChild(td2)
        tr.appendChild(td3)
        tr.appendChild(td4)
        tr.appendChild(td5)
        tabla.appendChild(tr) 
    }
}

let btnBuscar = document.getElementById("btnBuscar")
//función de buscar libro específico
btnBuscar.addEventListener("click",async function(){
    let idLibro = parseInt(document.getElementById("idLibro").value)
    if (isNaN(idLibro)) {
        alert("⚠️ Ingresa un ID válido")
        return
    }
    let encontrado = libros.find(libro=> libro.id == idLibro)
    if (encontrado){
        alert("Libro encontrado")
        document.getElementById("tituloLibro").value ="Titulo: "+ encontrado.titulo
        document.getElementById("autorLibro").value = "Autor: " + encontrado.autor
        document.getElementById("anioLibro").value = "Año: "+encontrado.anio
        document.getElementById("disponibleLibro").value = "Disponible: "+encontrado.disponible
    }else{
        alert("Error al extrar elementos X")
    }
})


let btnPrestar = document.getElementById("btnPrestar")
//función de prestar libro con patch
btnPrestar.addEventListener("click", async function(){
    let idLibro = parseInt(document.getElementById("idLibro").value)
    if (isNaN(idLibro)) {
        alert("⚠️ Ingresa un ID válido")
        return
    }
    try{
        let res = await fetch("http://localhost:3000/libros/"+idLibro,{
            method:"PATCH",
            headers:{"Content-Type":"application/json"},
            body: JSON.stringify({
                disponible:false
            })
        })
        let datos = await res.json();
        alert("Libro prestado, fecha de vencimiento: "+Date("22:11:19"))
        cargarDatos()
    }catch(error){
        alert("Error: "+error)
    }
})
let btnDevolver = document.getElementById("btnDevolver")
//función de devolver libro con PATCH
btnDevolver.addEventListener("click", async function(){
    let idLibro = parseInt(document.getElementById("idLibro").value)
    if (isNaN(idLibro)) {
        alert("⚠️ Ingresa un ID válido")
        return
    }
    try{
        let res = await fetch("http://localhost:3000/libros/"+idLibro,{
            method:"PATCH",
            headers:{"Content-Type":"application/json"},
            body: JSON.stringify({
                disponible:true
            })
        })
        let datos = await res.json();
        alert("Libro devuelto, fecha de devolución: "+Date("22:11:19"))
        cargarDatos()
    }catch(error){
        alert("Error: "+error)
    }
})

let btnConsultar = document.getElementById("btnConsultar")
let contenedor = document.getElementById("contenedor")
btnConsultar.addEventListener("click",async function(){
    contenedor.innerHTML = "" //limpiar contenedor
    let prestados = libros.filter(libro => libro.disponible === false);

    for (let prestado of prestados){
        let encabezado  = document.createElement("h2")
        encabezado.textContent = "Información del Libro"
        let p = document.createElement("p")
        p.textContent = "Título: "+prestado.titulo
        let p2 = document.createElement("p")
        p2.textContent = "Autor: "+prestado.autor
        let p3 = document.createElement("p")
        p3.textContent = "Año: "+prestado.anio
        contenedor.appendChild(encabezado)
        contenedor.appendChild(p)
        contenedor.appendChild(p2)
        contenedor.appendChild(p3)
    }


})
let btnAgregar = document.getElementById("btnAgregar")
//funciónde agregar libro con POST
btnAgregar.addEventListener("click", async function(){
    let tituloNuevo = document.getElementById("tituloNuevo").value
    let autorNuevo = document.getElementById("autorNuevo").value
    let anioNuevo = document.getElementById("anioNuevo").value
    if (
    tituloNuevo.trim() === "" ||
    autorNuevo.trim() === "" ||
    isNaN(anioNuevo)){
        alert("Error, ingresar todos los datos")
        return;
    }
    try{
        let res = await fetch("http://localhost:3000/libros",{
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify({
                titulo:tituloNuevo,
                autor:autorNuevo,
                anio:parseInt(anioNuevo),
                disponible:true
            })
        })
        if (!res.ok){
            throw new Error("Error al agregar Libro")
        }
        let datos = await res.json();
        alert("Libro agregado al sistema, Título: "+datos.titulo)
        await cargarDatos();
    }catch(error){
        alert("Error: "+error)
    }
})

let btnEliminar = document.getElementById("btnEliminar")
btnEliminar.addEventListener("click",async function(){
    let idEliminar = parseInt(document.getElementById("idEliminar").value)
    if (isNaN(idEliminar)){
        alert("Error: Introducir ID")
    }
    if (!libros.find(l => l.id == idEliminar)) {
    alert("Ese libro no existe")
    return
    }
    try{
        let res = await fetch("http://localhost:3000/libros/"+idEliminar,{
            method:"DELETE"
        })
        if (!res.ok){
            throw new Error("Error al eliminar Libro")
        }
        let datos = await res.json();
        alert("Libro eliminado correctamente") 
        cargarDatos();
    }catch(error){
        alert("Error: "+error)
    }
})