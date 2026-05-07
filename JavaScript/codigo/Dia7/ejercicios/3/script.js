function agregarTarea(idTarea){
    //extraemos elementos
    let tarea = document.getElementById("tarea")
    let lista = document.getElementById("listaTareas")
    let creado = document.createElement("li")
    creado.textContent = tarea.value
    creado.setAttribute("id",idTarea )
    //añadimos tarea a lista
    lista.appendChild(creado)
}

function borrarTarea(idTarea){
    
}

