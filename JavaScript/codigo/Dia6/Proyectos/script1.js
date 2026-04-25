let elementoLongitud = document.getElementById("tieneLongitud")
let elementoNumeros =document.getElementById("tieneNumeros")
let elementoMayusculas = document.getElementById("tieneMayusculas")
let elementoResultado = document.getElementById("resultado")
function validarContraseña(){
    let contraseña = document.getElementById("contraseña").value
    let tieneLongitud = contraseña.length > 7
    let tieneNumeros = /[0-9]/.test(contraseña)
    let tieneMayusculas = /[A-Z]/.test(contraseña)
    if (tieneLongitud){
        elementoLongitud.textContent = "Bien, tiene más de 8 carácteres"
    } else{elementoLongitud.textContent = "Debe tener al menos 8 carácteres"

    }
    // Resultado final
    if (tieneLongitud && tieneNumeros && tieneMayusculas) {
        elementoResultado.textContent = "🔒 Contraseña fuerte"
    } else {
        elementoResultado.textContent = "🔓 Contraseña débil, corrige los puntos marcados"
    }

}