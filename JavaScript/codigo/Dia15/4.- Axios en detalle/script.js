let datos = {
    title: "Nuevo post",
    body: "Mi contenido"
}
 //interceptores en axios - de pedido
let miToken =  "mi_token"
axios.interceptors.request.use(
    (config) =>{
        config.headers.Authorization = 'Bearer'+miToken
        return config;
    }, (error) =>{
        return Promise.reject(error);
    })

//interceptores de respuesta
axios.interceptors.response.use(
    (respuesta)=>{
        respuesta.data.customField = "Nuevo campo"
        return respuesta
    },(error)=>{
        return Promise.reject(error)
    }
)
let pedido1 = axios.get("https://api.ejemplo.com/data1")
let pedido2 = axios.get("https://api.ejemplo.com/data2")
let pedido3 = axios.get("https://api.ejemplo.com/data3")


axios.post("https://jsonplaceholder.typicode.com/posts")
.then(respuesta =>{
    console.log("Post creado con éxito",respuesta.data)
})
.catch(error=>{
    console.log(error)
})

async function obtenerDatos(){
    try{
        let res  = await axios.all(pedido1,pedido2,pedido3) //toma array de promesas
    let data = await axios.spread((respuesta1,respuesta2,respuesta3) =>{
        //codigo
    })
    }catch(error){
        alert("Error: ",error)
    }
    
}
 //cuando todas las promesas se hayan resuelto

