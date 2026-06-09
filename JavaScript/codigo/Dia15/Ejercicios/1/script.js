// ── Sección 1: buscar post por ID ──────────────────────────────
async function extraerPost(id) {
    try {
        let respuesta = await fetch("https://jsonplaceholder.typicode.com/posts/" + id)
        if (!respuesta.ok) {
            throw new Error("Error: " + respuesta.statusText)
        }
        let datos = await respuesta.json()
        return datos
    } catch (error) {
        alert("Error: " + error)
    }
}

let input     = document.getElementById("input")
let btn       = document.getElementById("btn")
let titulo    = document.getElementById("titulo")
let contenido = document.getElementById("contenido")

btn.addEventListener("click", async function () {
    let id    = input.value
    let datos = await extraerPost(id)
    titulo.textContent    = "Título: "    + datos.title
    contenido.textContent = "Contenido: " + datos.body
})


// ── Sección 2: CRUD ────────────────────────────────────────────
let datosContenedor = document.getElementById("datosObtenidos")

// FIX 2: renombrar parámetro "datos" → "datosEntrada" para evitar colisión
async function gestionarPost(accion, id, datosEntrada) {

    if (accion === "obtener") {
        let res  = await fetch("https://jsonplaceholder.typicode.com/posts/" + id)
        let dato = await res.json()
        // FIX 1: es un objeto, no un array → sin for...of
        datosContenedor.innerHTML = ""
        let li = document.createElement("li")
        li.textContent = dato.title
        datosContenedor.appendChild(li)
        alert("Datos obtenidos")

    } else if (accion === "crear") {
        let [tituloVal, contenidoVal] = datosEntrada
        let res  = await fetch("https://jsonplaceholder.typicode.com/posts", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ title: tituloVal, body: contenidoVal, userId: 1 })
        })
        let dato = await res.json()
        // FIX 1: POST también devuelve un objeto, no un array
        datosContenedor.innerHTML = ""
        let li = document.createElement("li")
        li.textContent = dato.title
        datosContenedor.appendChild(li)
        alert("Datos creados")

    } else if (accion === "actualizar") {
        let [tituloVal, contenidoVal] = datosEntrada
        let res  = await fetch("https://jsonplaceholder.typicode.com/posts/" + id, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ title: tituloVal, body: contenidoVal })
        })
        let dato = await res.json()
        // FIX 3: nunca asignes un objeto directo a textContent
        datosContenedor.textContent = "Título actualizado: " + dato.title
        alert("Datos actualizados")

    } else {
        let res = await fetch("https://jsonplaceholder.typicode.com/posts/" + id, {
            method: "DELETE"
        })
        await res.json()
        // FIX 3: DELETE devuelve {} → confirma con un mensaje tuyo
        datosContenedor.textContent = "Post " + id + " eliminado correctamente"
        alert("Datos eliminados")
    }
}


// ── Eventos selector y btn2 ────────────────────────────────────
let selector  = document.getElementById("selector")
let input2    = document.getElementById("input2")
let btn2      = document.getElementById("btn2")
let seleccion = "obtener"

selector.addEventListener("change", function (e) {
    seleccion = e.target.value
    let contenedor = document.getElementById("contenedor")
    contenedor.innerHTML = ""

    // FIX 4: la condición estaba negada con ! → corregida a !==
    if (e.target.value !== "obtener") {
        contenedor.innerHTML = `
            <label>Título: <input type="text" id="tituloInput"></label>
            <label>Contenido: <input type="text" id="contenidoInput"></label>
        `
    }
})

btn2.addEventListener("click", function () {
    let id = input2.value
    // FIX 5: leer .value del elemento, no el elemento en sí
    let tituloVal    = document.getElementById("tituloInput")?.value   || ""
    let contenidoVal = document.getElementById("contenidoInput")?.value || ""
    // FIX 5: pasar [titulo, contenido] como array, que es lo que espera la función
    gestionarPost(seleccion, id, [tituloVal, contenidoVal])
})