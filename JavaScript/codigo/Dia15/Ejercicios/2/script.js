let lista = document.getElementById("listaUsuarios");

async function obtenerDatos(){
    try{
        let res = await fetch("https://jsonplaceholder.typicode.com/users")
        let datos = await res.json();
        return datos
    } catch(error){
        alert("Error: "+error)
    }

}

async function mostrarDatos(){
    datos =await  obtenerDatos()
    for (let data of datos){
        let li = document.createElement("li");
        li.textContent = "Nombre: "+data.name+" - Email: "+data.email+" - Ciudad: "+data.address.city
        lista.appendChild(li)

    }
}