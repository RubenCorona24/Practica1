let usuario = "Ruben" //usuario para credencial
let password = "javascriptTotal" //password para credencial


//Función de obtener datos con credenciales
async function obtenerDatos(){
    let respuesta = await fetch("https://jsonplaceholder.typicode.com/posts",{
        method:"GET",
        credentials: "include", //incluimos credenciales
        headers: {
            'Authorization': "Basic"+btoa(usuario+":"+password),
            'Content-Type': "application/json"
        }
    })
    let datos = await respuesta.json();
    console.log(datos)
}

let token = "miToken"
//Función de obtener datos con credenciales **con Bearer**
async function obtenerDatos2(){
    let respuesta = await fetch("https://jsonplaceholder.typicode.com/posts",{
        method:"GET",
        credentials: "include", //incluimos credenciales
        headers: {
            'Authorization': "Bearer"+token, //usamos token
            'Content-Type': "application/json"
        }
    })
    let datos = await respuesta.json();
    console.log(datos)
}
obtenerDatos2()

//uso de cache en fetch
async function obtenerDatosCache(){
    let respuesta = await fetch("https://jsonplaceholder.typicode.com/posts",{
        method:"GET",
        credentials: "include", 
        cache: "default", //uso de cache determinado
        headers: {
            'Authorization': "Basic"+btoa(usuario+":"+password),
            'Content-Type': "application/json"
        }
    })
    let datos = await respuesta.json();
    console.log(datos)


}
//alternativas de caché: 
//1- no cache: siempre realiza solicitud de servidor
//2- no-store: no va a almacenar la información en el caché
//3- reload: forzar al navegador a descargar el recurso
//4- force-cache: utilizar siempre la copia en caché
//5- only-if-cached: solo utiliza la copia que se encuentra en cache si está disponible


//manejo de redirecciones
async function obtenerDatosRedirect(){
    let respuesta = await fetch("https://jsonplaceholder.typicode.com/posts",{
        method:"GET",
        credentials: "include",
        redirect: "follow", //valor determinado
        headers: {
            'Authorization': "Basic"+btoa(usuario+":"+password),
            'Content-Type': "application/json"
        }
    })
    let datos = await respuesta.json();
    console.log(datos)
}

//alternativvas de redirect
//1- error: rechaza con tipo de error typerror apenas se redirecciona
//2- manual: devuelve el codigo de la promesa - programas el casos

async function obtenerDatosRedirect2(){
    let respuesta = await fetch("https://jsonplaceholder.typicode.com/posts",{
        method:"GET",
        credentials: "include",
        redirect: "manual", //valor determinado
        headers: {
            'Authorization': "Basic"+btoa(usuario+":"+password),
            'Content-Type': "application/json"
        }
    })
    if (respuesta.type === "opaqueredirect"){
        let nuevaUbicacion = respuesta.headers.get("Location")
        console.log("Redirigiendo a: "+nuevaUbicacion)
    }
    let datos = await respuesta.json();
    console.log(datos)
}
