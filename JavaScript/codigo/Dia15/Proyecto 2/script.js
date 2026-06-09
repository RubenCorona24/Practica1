let tabla = document.getElementById("tbody")
let tareas = []
//cargar todas las tareas
async function cargarTareas(){
    tabla.innerHTML = ""
    try{
        let res = await fetch("http://localhost:3000/tareas");
        if (!res.ok){
            throw new Error("Error al cargar datos")
        }
        let datos = await res.json();
        tareas = datos;
        //cargar elementos
        for (let tarea of datos){
            let tr = document.createElement("tr")
            let td = document.createElement("td")
            td.textContent = tarea.id
            let td2 = document.createElement("td")
            td2.textContent = tarea.titulo
            let td3 = document.createElement("td")
            td3.textContent = tarea.estado
            tr.appendChild(td)
            tr.appendChild(td2)
            tr.appendChild(td3)
            tabla.appendChild(tr)
            

        }
    }catch(error){
        alert("Error: "+error )
    }
}

let btnBuscar = document.getElementById("btnBuscar")
btnBuscar.addEventListener("click", async function() {
    let idTarea = parseInt(document.getElementById("idTarea").value)
    if (isNaN(idTarea)){
        alert("Error: Ingresar un ID")
        return;
    }
    try{
        let res = await fetch(`http://localhost:3000/tareas/${idTarea}`)
    if (!res.ok){
        throw new Error("Error al buscar id de tarea")
    }
    let datos = await res.json();
    document.getElementById("idText").textContent = datos.id
    document.getElementById("tituloText").textContent = datos.titulo
    document.getElementById("estadoText").textContent = datos.estado
    }catch(error){
        alert("Error: "+ error)
    }
})

let btnModificar = document.getElementById("btnModificar")
btnModificar.addEventListener("click",async function(){
    let id = parseInt(document.getElementById("idTarea").value )//repetimos input
    let nuevoTitulo = document.getElementById("nuevoTitulo").value
    let nuevoEstado = document.getElementById("nuevoEstado").value
    if (isNaN(id)){
        alert("Error: Ingresar un ID")
        return;
    }
    try{
        let res = await fetch(`http://localhost:3000/tareas/${id}`,{
            method:"PUT",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify({
                id:id,
                titulo:nuevoTitulo,
                estado:nuevoEstado
            })
        })
        if (!res.ok){
            throw new Error("Error al modificar tarea")
        }
        let datos = await res.json();
        alert("Datos modificados correctamente")
    }catch(error){
        alert("Error al modificar: "+error)
    }
})

let btnEliminar = document.getElementById("btnEliminar")
btnEliminar.addEventListener("click",async function(){
    let id = parseInt(document.getElementById("idTarea").value)
    if (isNaN(id)){
        alert("Error: Ingresar un ID")
        return;
    }
    try{
        let res = await fetch(`http://localhost:3000/tareas/${id}`,{
            method:"DELETE"
        })
        if (!res.ok){
            throw new Error("Error al eliminar tarea")
        }
        let datos = await res.json();
        document.getElementById("idText").textContent = ""
        document.getElementById("tituloText").textContent = ""
        document.getElementById("estadoText").textContent = ""
        alert("Datos eliminados: "+JSON.stringify(datos))
    }catch(error){
        alert("Error: "+error)
    }
})