//extraer elementos html
let inputMoneda = document.getElementById("inputMoneda")
let boton = document.getElementById("btnCalcular")
let span = document.getElementById("moneda")
let spanNombre = document.getElementById("nombre")
let spanPais = document.getElementById("pais")
let spanEmail = document.getElementById("email")
let img = document.getElementById("imagen");

inputMoneda.addEventListener("keydown",function(e){
    if ((e.keyCode < 65 || e.keyCode > 90) && e.keyCode != 32 && e.keyCode !=8){
        e.preventDefault()
    }
})
async function obtenerDatos() {
    try{
        let moneda = inputMoneda.value.toUpperCase();
        let res = await fetch("https://open.er-api.com/v6/latest/USD");
        let datos = await res.json();

        let resUsuario = await fetch("https://randomuser.me/api/");
        let datosUsuario = await resUsuario.json();
        
        if (!datos.rates[moneda]){
            span.textContent = "⚠️ Moneda no encontrada" //mensaje error
            return
        }
        span.textContent = datos.rates[moneda]
        spanNombre.textContent = datosUsuario.results[0].name.first;
        spanPais.textContent = datosUsuario.results[0].location.country;
        spanEmail.textContent = datosUsuario.results[0].email;
        img.src = datosUsuario.results[0].picture.large
    } catch(error){
        span.textContent = "❌ Error al obtener datos"
    }    
}
boton.addEventListener("click",obtenerDatos)