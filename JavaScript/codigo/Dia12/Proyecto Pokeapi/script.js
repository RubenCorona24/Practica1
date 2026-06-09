//extrar elementos html
let input = document.getElementById("nombre")
let boton = document.getElementById("btnBuscar")
let botonAleatorio = document.getElementById("btnAleatorio")
let contenedor = document.getElementById("contenedor")
let nombreSpan = document.getElementById("nombreSpan")
let listaHabiliadades = document.getElementById("listaHabilidades")
let experienciaSpan = document.getElementById("experienciaSpan")
let pesoSpan = document.getElementById("pesoSpan")
let alturaSpan = document.getElementById("alturaSpan")
let listaTipos = document.getElementById("listaTipos")
//eventos

input.addEventListener("keydown",function(e){
    if ((e.keyCode < 65 || e.keyCode > 90) && e.keyCode != 32 && e.keyCode !=8){
        e.preventDefault()
    }
})

boton.addEventListener("click",function(){
    if (input.value.trim() === "") {
        alert("⚠️ Escribe el nombre de un pokemon")
        return
    }
    let nombre = input.value
    listaHabiliadades.innerHTML = ""
    contenedor.innerHTML = ""
    listaTipos.innerHTML = ""
    fetch("https://pokeapi.co/api/v2/pokemon/"+nombre)
    .then(response=>response.json())
    .then(data=>{
        nombreSpan.textContent = data.name
        for (let item of data.abilities){
            let li = document.createElement("li")
            li.textContent = item.ability.name
            listaHabiliadades.appendChild(li) //agregamos habilidades
        }
        experienciaSpan.textContent = data.base_experience
        let img = document.createElement("img")
        img.setAttribute("src",data.sprites.front_default)
        contenedor.appendChild(img) //agregamos imagen
        pesoSpan.textContent = data.weight/10 + " kilogramos"
        alturaSpan.textContent = data.height/10 + " metros"
        //tipos
        for (let type of data.types){
            let li = document.createElement("li")
            li.textContent = type.type.name
            listaTipos.appendChild(li)
        }
        
    })
    .catch(error=>{
        alert("Pokemon No encontrado❌")
    })
})
botonAleatorio.addEventListener("click",function(){
    listaHabiliadades.innerHTML = ""
    contenedor.innerHTML = ""
    listaTipos.innerHTML = ""
    let idAleatorio = Math.floor(Math.random()*(1025-1+1))+1
    fetch("https://pokeapi.co/api/v2/pokemon/"+idAleatorio)
    .then(response=>response.json())
    .then(data=>{
        nombreSpan.textContent = data.name
        for (let item of data.abilities){
            let li = document.createElement("li")
            li.textContent = item.ability.name
            listaHabiliadades.appendChild(li) //agregamos habilidades
        }
        experienciaSpan.textContent = data.base_experience
        let img = document.createElement("img")
        img.setAttribute("src",data.sprites.front_default)
        contenedor.appendChild(img) //agregamos imagen
        pesoSpan.textContent = data.weight/10 + " kilogramos"
        alturaSpan.textContent = data.height/10 + " metros"
        //tipos
        for (let type of data.types){
            let li = document.createElement("li")
            li.textContent = type.type.name
            listaTipos.appendChild(li)
        }
    }
)

})
