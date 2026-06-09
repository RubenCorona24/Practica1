//obtener datos
let titulo = document.getElementById("titulo")
let imagen = document.getElementById("imagen")
let parrafo1 = document.getElementById("parrafo1")
let parrafo2 = document.getElementById("parrafo2")
let parrafo3 = document.getElementById("parrafo3")
function iniciarSitio(){
    cargarElementos();
    obtenerDatos();
}
//consultar APIS externas

async function obtenerDatos(){
    try{
        const respuestaDolarEuro = await fetch("https://open.er-api.com/v6/latest/USD");
    const datosDolarEuro = await respuestaDolarEuro.json()

    const respuestaDolarArs = await fetch("https://open.er-api.com/v6/latest/ARS");
    const datosDolarArs = await respuestaDolarArs.json()
    parrafo1.textContent = "Dolar respecto a Euro: "+datosDolarEuro.rates['EUR']+" USD dólares"
    parrafo2.textContent = "Dolar respecto a pesos Argentinos: "+datosDolarArs.rates['USD']+" ARS pesos argentinos"
    document.getElementById("gif").style.display = "none" //ocultamos gif
    } catch(error){
        alert("Error: "+error)
    }
    
}

//mostrar la información obtenida en el HTML
function cargarElementos(){
    titulo.textContent = "Cotización de monedas"
    imagen.src = "monedas.jpg"

}
