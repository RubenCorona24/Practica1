//extraer elementos
let input = document.getElementById("pais")
let boton = document.getElementById("btnBuscar")
let conteendor = document.getElementById("contenedor")

//evento de input

input.addEventListener("keydown", function(e) {
    if (e.keyCode < 31 || e.keyCode > 128) {
        if (e.key === "Backspace" || e.key === "Delete") {
            return
        } else {
            e.preventDefault()
        }
    }
})

//evento de boton
boton.addEventListener("click",function(e){
    if (input.value.trim() === "") {
        alert("⚠️ Escribe el nombre de un país")
        return
    }
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
        imagen.setAttribute("src",data[0].flags.png)
        conteendor.appendChild(nombre)
        conteendor.appendChild(capital)
        conteendor.appendChild(continente)
        conteendor.appendChild(imagen)
        let descripcion = document.createElement("h2")
        descripcion.textContent = "Descripción General"
        conteendor.appendChild(descripcion)
        let p = document.createElement("p")
        let mensaje;
        if (data[0].independent === true){
            mensaje = "Estado Independiente"
            p.style.color = "green"
        }else{
            mensaje = "Estado No Independiente"
            p.style.color = "red"
        }
        p.textContent = mensaje
        p.setAttribute("id","estado")
        conteendor.appendChild(p)
        let poblacion = document.createElement("p")
        poblacion.textContent = "Población: "+data[0].population.toLocaleString()
        conteendor.appendChild(poblacion)
        let idiomas = Object.values(data[0].languages) //objeto
        let idioma = document.createElement("p")
        idioma.textContent = "Idiomas: "+idiomas.join(", ") //utilizamos método join con separador ", "
        conteendor.appendChild(idioma)
        let area = document.createElement("p")
        area.textContent = "Área: "+data[0].area.toLocaleString()+" km²"
        conteendor.appendChild(area)
        //evento de mouseover en descripcion
        descripcion.addEventListener("mouseover",function(){
            p.style.display = "block";
            poblacion.style.display = "block";
            idioma.style.display = "block";
            area.style.display = "block";
        })
        descripcion.addEventListener("mouseout",function(){
            p.style.display = "none";
            poblacion.style.display = "none";
            idioma.style.display = "none";
            area.style.display = "none";
        })
        p.style.display = "none";
        poblacion.style.display = "none";
        idioma.style.display = "none";
        area.style.display = "none";


        

    })
    .catch(error =>{
        conteendor.innerHTML = "<p style='color:red'>⚠️ País no encontrado</p>" //en caso de país no encontrado
    })
})
