//accedemos a los elementos 
let boton = document.getElementById("btnBuscar")
let input = document.getElementById("nombre")
//accedemos a datos de json
let datos;
fetch("datos.json")
.then(response=>response.json())
.then(data=>{
    datos = data;
})
//evento de keydown en input
input.addEventListener("keydown",function(e){
    if (e.keyCode < 31 || e.keyCode > 128 ){
        if (e.key === "Backspace" || e.key === "Delete") {
            return  // ← dejar pasar
            }else{
                e.preventDefault(); //Evita el evento por defecto
            }
    }
})
//evento de click en boton
boton.addEventListener("click",function(){
    let contenedor = document.getElementById("contenedor")
    let nombre = input.value
    contenedor.innerHTML = ""
    for (let user of datos.data){
        if (user.nombre.includes(nombre)){
            alert("Usuario encontrado ")
            let ul = document.createElement("ul")
            let li = document.createElement("li")
            li.textContent = user.nombre
            let li2 = document.createElement("li")
            li2.textContent = user.telefono
            let li3 = document.createElement("li")
            li3.textContent = user.email
            ul.appendChild(li)
            ul.appendChild(li2)
            ul.appendChild(li3)
            contenedor.appendChild(ul)
        }
    }
    
})