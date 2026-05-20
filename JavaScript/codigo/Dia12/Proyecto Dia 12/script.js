//extrar elementos html
let selector = document.getElementById("selector")
let boton = document.getElementById("botonBuscar")
let peliculaInput = document.getElementById("peliculaInput")
let datos;
//escuchador de eventos al selector
selector.addEventListener("change",function(e){
    let seleccion = e.target.value
    if (seleccion === "Series"){
        datos = "series.json"
        alert("Fuente de búsqueda: series.json")
    }else{
        datos = "peliculas.json"
        alert("Fuente de búsqueda: peliculas.json")
    }
})

//evento para input: solo admite letras, espacio y borrar (keydown event)
peliculaInput.addEventListener("keydown",function(e){
    if (e.keyCode < 31 || e.keyCode > 128 ){
        if (e.key === "Backspace" || e.key === "Delete") {
            return  // ← dejar pasar
            }else{
                e.preventDefault(); //Evita el evento por defecto
            }
    }
})
//boton vigilar evento click
boton.addEventListener("click",function(){
    if (!datos) {
        alert("⚠️ Selecciona Series o Películas primero")
        return
    }
    fetch(datos)
    .then(response => response.json())
    .then(data=>{
        let ul = document.getElementById("lista")
        ul.innerHTML = ""
        for (let objeto of data.data){
            if (objeto.nombre.includes(peliculaInput.value.toUpperCase())){
                let p = document.createElement("p")
                p.textContent = objeto.sinopsis
                let li = document.createElement("li")
                li.textContent = objeto.nombre
                // ✅ ocultar sinopsis por defecto
                p.style.display = "none"

        // ✅ mouseover — mostrar sinopsis
                li.addEventListener("mouseover", function() {
                    p.style.display = "block"
                })

        // ✅ mouseout — ocultar sinopsis
                li.addEventListener("mouseout", function() {
                    p.style.display = "none"
                })
                ul.appendChild(li)
                ul.appendChild(p)
            }
        }
    })
    .catch(error =>{
        alert(error);
    })
})
//etiqueta ul

//obtener datos json

//recorrer el array y verificar coincidencias parciales o totales (startsWith), y usar toUpperCase

//en cada iteración verificar que "nombre" coincida con el ingreso del usuario

//si coincide, crear un <p> para almacenar la sinopsis, y un <li> para almacenar el nombre, <p> se adjuntará a <li>

//2 eventos para <li>: mouseover y mouseout

//Luego, en nuestra página HTML se deberá declarar una etiqueta input y un botón. Al input, para el evento keydown, se debe verificar que solo se ingresen letras. Para esto, la propiedad event.key del teclado tiene que estar entre 65 y 90. Como dato extra, para incluir espacios y permitir borrar se deben permitir los códigos 8 y 32. Al botón, para el evento click, se debe llamar a una función para realizar la búsqueda.