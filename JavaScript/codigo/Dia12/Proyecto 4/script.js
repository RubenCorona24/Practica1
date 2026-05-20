//extraer elementos
let input = document.getElementById("pais")
let boton = document.getElementById("btnBuscar")
let conteendor = document.getElementById("contenedor")

//evento de input
input.addEventListener("keydown",function(e){
    if (e.keyCode < 31 || e.keyCode > 128 ){
        if (e.key === "Backspace" || e.key === "Delete") {
            return  // ← dejar pasar
            }else{
                e.preventDefault(); //Evita el evento por defecto
            }
    }
})

//evento de boton
boton.addEventListener("click",function(e){
    conteendor.innerHTML = ""
    let pais = input.value
    fetch("https://restcountries.com/v3.1/name/"+pais)
    .then(response=>response.json())
    .then(data=>{
        console.log(data)
        let nombre = document.createElement("p")
        nombre.textContent = "País: "+pais
        let capital = document.createElement("p")
        capital.textContent = "Capital: "+data[0].capital
        let continente = document.createElement("p")
        continente.textContent = "Continente: "+data[0].continents
        let imagen = document.createElement("img")
        imagen.setAttribute("src",pais+".png")
        conteendor.appendChild(nombre)
        conteendor.appendChild(capital)
        conteendor.appendChild(continente)
        conteendor.appendChild(imagen)
        let descripcion = document.createElement("h2")
        descripcion.textContent = "Descripción General"
        conteendor.appendChild(descripcion)

    })
})
