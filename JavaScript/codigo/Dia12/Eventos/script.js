//extraemos elementos
let boton = document.getElementById("boton")
let texto = document.getElementById("texto")
let contenedor = document.getElementById("contenedor")
//agregar eventos a los elementos

//elemento para boton
boton.addEventListener("click",function(){
    alert("Botón presionado✅")
})

//evento para texto
texto.addEventListener("mouseover",function(){
    alert("Seleccionaste el texto con el cursor✅")
})