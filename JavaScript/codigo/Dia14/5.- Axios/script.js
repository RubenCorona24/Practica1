function obtenerInformacion(){
    axios.get("https://jsonplaceholder.typicode.com/posts")
    .then(respuesta=>{
        let lista = document.getElementById("listaInformacion");
        for (let i=0;i<respuesta.data.length;i++){
            let itemLista = document.createElement("li");
            itemLista.textContent = respuesta.data[i].title;
            lista.appendChild(itemLista)
        }
    })
    .catch(error=>{
        console.log(error) //imprime el error
    })
}