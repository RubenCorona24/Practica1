//extraer elementos html
let menu = document.getElementById("menu")
let boton = document.getElementById("boton")

//añadir escuchador de eventos al boton
boton.addEventListener("mouseover",function(){
    menu.style.display = 'block' //reanudamos opciones
})
boton.addEventListener("mouseout",function(){
    menu.style.display = 'none' //reanudamos opciones
})

//evento de movimiento del mouse en el documento
document.addEventListener("mousemove",function(e){
    console.log("Posición X: "+e.clientX+" - Posición Y: "+e.clientY)
})