

//página que administra un registro de disposiitovs moviles de un servidor
let dispositivos = [] //array global


async function cargarDispositivos() {
    try{
        let res = await fetch("https://my-json-server.typicode.com/fedegaray/telefonos/db");
        if(!res.ok){
            throw new Error("Error")
        }
        let datos = await res.json();
        dispositivos = datos.dispositivos
        mostrarRegistros()
    }catch(error){
        alert(error)
    }
}


//operaciones crud: consultar,moduficar,agregar,eliminar

//contar con 5 llamadas al servidor

//1.- Mostrar todos los registros con elemento table html
//1.- consultar cada registro individual (GET) elemento input de id y boton cunsultar
//textarea elemento html
//agregar registros nuevos (POST) 5 elementos input - mostrar solo alert
//4.- modificar registros existentes (PUT) - mostrar alert
//5.- eliminar registros (DELETE) - mostrar alert
//GET POST: GENERAL: url normal
//PUT,DELETE,GET(INDIVIDUAL): Agregar id al url de base

//extraer elementos html
let tabla = document.getElementById("tabla")

async function mostrarRegistros(){
    tabla.innerHTML = "" //limpiar tabla
    for (dispositivo of dispositivos){
        let tr = document.createElement("tr")
        let td = document.createElement("td")
        td.textContent = dispositivo.id
        let td2 = document.createElement("td")
        td2.textContent = dispositivo.marca
        let td3 = document.createElement("td")
        td3.textContent = dispositivo.modelo
        let td4 = document.createElement("td")
        td4.textContent = dispositivo.color
        let td5 = document.createElement("td")
        td5.textContent = dispositivo.almacenamiento
        let td6 = document.createElement("td")
        td6.textContent = dispositivo.procesador
        let elementos = [tr,td,td2,td3,td4,td5,td6]
        tr.appendChild(td)
        tr.appendChild(td2)
        tr.appendChild(td3)
        tr.appendChild(td4)
        tr.appendChild(td5)
        tr.appendChild(td6)
        tabla.appendChild(tr) 
    }
    
}
let resultado = document.getElementById("resultado")
let btn = document.getElementById("btnBuscar")
btn.addEventListener("click",async function(){
    let id = parseInt(document.getElementById("id").value)
    if (isNaN(id)) {
        alert("⚠️ Ingresa un ID válido")
        return
    }

    // buscar en el array que ya tienes cargado
    let encontrado = dispositivos.find(d => d.id === id)

    let textarea = document.getElementById("resultado")

    if (encontrado) {
        // JSON.stringify(objeto, null, 2) formatea bonito el JSON
        textarea.value = textarea.value = 
        "ID: " + encontrado.id + "\n" +
        "Marca: " + encontrado.marca + "\n" +
        "Modelo: " + encontrado.modelo + "\n" +
        "Color: " + encontrado.color + "\n" +
        "Almacenamiento: " + encontrado.almacenamiento + "\n" +
        "Procesador: " + encontrado.procesador
    } else {
        textarea.value = "❌ Dispositivo con ID " + id + " no encontrado"
    }
    
})
//función de agregar dispositivo
async function agregarDispositivo(){
    let marcaInput = document.getElementById("inputMarca").value
    let modeloInput = document.getElementById("inputModelo").value
    let colorInput = document.getElementById("inputColor").value
    let almacenamientoInput = document.getElementById("inputAlmacenamiento").value
    let procesadorInput = document.getElementById("inputProcesador").value
    let nuevoDispositivo = {
        marca: marcaInput,
        modelo:modeloInput,
        color:colorInput,
        almacenamiento:almacenamientoInput,
        procesador:procesadorInput
    }
    let res = await fetch("https://my-json-server.typicode.com/fedegaray/telefonos/db",{
        method: "POST",
        headers: {
            "Content-Type":"application/json"
        },
        body: JSON.stringify(nuevoDispositivo)
    })
    let datos = await res.json()
    alert("Dispositivo agregado: "+JSON.stringify(datos))
    
}

//función de modoficar dispositivo-
async function modificarInformacion(){
    let id = parseInt(document.getElementById("idDispositivo").value)
    let actualizado = {
        marca: document.getElementById("putMarca").value,
        modelo: document.getElementById("putModelo").value,
        color: document.getElementById("putColor").value,
        almacenamiento: document.getElementById("putAlmacenamiento").value,
        procesador: document.getElementById("putProcesador").value
    }
    try{
        let res = await fetch("https://my-json-server.typicode.com/fedegaray/telefonos/dispositivos/"+id,{
            method:"PUT",
            headers:{
                "Content-Type":"application/json"
            },
            body: JSON.stringify(actualizado)
        });
        if(!res.ok){
            throw new Error("Error")
        }
        let datos = await res.json();
                let index = dispositivos.findIndex(d => d.id === id)
        dispositivos[index] = { id: id, ...actualizado }
        mostrarRegistros()
        alert("✅ Modificado: " + JSON.stringify(datos))

    }catch(error){
        alert(error)
    }
}

//función de eliminar un registro
async function eliminarRegistro(){
    let idEliminar = document.getElementById("idEliminar").value
    try{
        let res = await fetch("https://my-json-server.typicode.com/fedegaray/telefonos/dispositivos/"+idEliminar,{
            method:"DELETE"
        })
        if (res.ok){
            dispositivos = dispositivos.filter(d => d.id !== idEliminar)  // ✅ idEliminar
            mostrarRegistros()
            alert("✅ Eliminado correctamente")
        }
    }catch(error){
        alert("Error: "+error)
    }
}
let btnEliminar = document.getElementById("btnEliminar")
btnEliminar.addEventListener("click",eliminarRegistro)