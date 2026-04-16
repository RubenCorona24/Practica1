//extraemos los elementos
let elementoEdad = document.getElementById("edad")
let  elementoR1 = document.getElementById("respuesta1")
let elementoR2 = document.getElementById("respuesta2")
let elementoR3 = document.getElementById("respuesta3")
//creamos funciones

function calcular(){
    let edad = parseInt(elementoEdad.value)  // ← leer aquí, no afuera
    let puedeBeber = edad >= 18;
    elementoR1.textContent = puedeBeber;
    let puedeIngresar = edad >=18  && edad<=30;
    elementoR2.textContent = puedeIngresar
    let entradaGratis = edad==20  || edad ==25
    elementoR3.textContent = entradaGratis;
}
