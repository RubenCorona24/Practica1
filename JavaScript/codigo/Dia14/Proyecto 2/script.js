let spanMx = document.getElementById("spanMX")
let spanEUR = document.getElementById("spanEUR")
let spanARS = document.getElementById("spanARS")
let selector = document.getElementById("selector")
let pais = "Mexico";
let spanGrados = document.getElementById("gradosC")
let spanHumedad = document.getElementById("humedad")
let spanEstado = document.getElementById("estado")
let nombreOperador = document.getElementById("nombreOperador")
let apellidoOperador = document.getElementById("apellidoOperador")
let imagen = document.getElementById("imagen")

selector.addEventListener("change",function(){
    let seleccion = selector.value
    pais = seleccion
    alert("Datos de clima de "+seleccion)
    cargarDatos()
})

async function cargarDatos(){
    try{
            let [datosCotizaciones, datosClima,datosUsuario] = await Promise.all([
            fetch("https://open.er-api.com/v6/latest/USD").then(r => r.json()),
            fetch("https://wttr.in/" +pais+ "?format=j1").then(r => r.json()),
            fetch("https://randomuser.me/api/").then(r=>r.json())
            ])

        //actualizamos información
        spanMx.textContent = datosCotizaciones.rates['MXN'];
        spanEUR.textContent = datosCotizaciones.rates["EUR"];
        spanARS.textContent = datosCotizaciones.rates["ARS"];
        //información de clima
        spanGrados.textContent = datosClima.current_condition[0].FeelsLikeC;
        spanHumedad.textContent = datosClima.current_condition[0].humidity;
        spanEstado.textContent = datosClima.current_condition[0].lang_es[0].value;
        //Información de usuario
        nombreOperador.textContent = datosUsuario.results[0].name.first;
        apellidoOperador.textContent = datosUsuario.results[0].name.last;
        imagen.src = datosUsuario.results[0].picture.large;
    }catch(error){
        alert("Error: "+error)
    }
    

}