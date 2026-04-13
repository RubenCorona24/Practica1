let elementoResultado = document.getElementById("resultado") //check
let elementoNum1 = document.getElementById("num1") //check
let elementoNum2 = document.getElementById("num2") //check
function mostrarResultado(resultado){
    elementoResultado.textContent = resultado
}

function obtenerValores(){ //función de devolver valores
    let num1 = parseInt(elementoNum1.value)
    let num2 = parseInt(elementoNum2.value)
    return {num1,num2}

}
function esValido(...numeros) {
    return numeros.every(n => !isNaN(n))
}

function sumar(){
    let {num1,num2} = obtenerValores()
    let r = num1 + num2
    mostrarResultado(r)
}
function restar(){
    let {num1,num2} = obtenerValores()
    let r = num1-num2
    mostrarResultado(r)
}
function multiplicar(){
    let {num1,num2} = obtenerValores()
    let r = num1 * num2
    mostrarResultado(r)
}
function dividir(){
    let {num1,num2} = obtenerValores()
    if (num2 === 0) {
        mostrarResultado("Error: NO dividir entre 0")
        return //detiene la ejecución
    }
    let r = (num1 / num2).toFixed(2)
    mostrarResultado(r)
}
function sacarRaiz(){
     let { num2 } = obtenerValores()
     if (num2<0){
        mostrarResultado("Error: no existe raíz de números negativos")
        return //detiene la eejcución
     }
     let r = Math.sqrt(num2).toFixed(4)
     mostrarResultado(r)
}
function sacarPotencia(){
    let { num1,num2 } = obtenerValores()
    let r = Math.pow(num1,num2)
    mostrarResultado(r)
}
function sacarAbsoluto(){
    let { num2 } = obtenerValores()
    let r = Math.abs(num2)
    mostrarResultado(r)
}
function sacarRandom(){
    let { num1,num2 } = obtenerValores()
    let numRandom = Math.floor(Math.random() * (num2-num1+2)) + num1
    mostrarResultado(numRandom)
}
function redondearAlPiso(){
    let { num2 } = obtenerValores()
    let r = Math.floor(num2)
    mostrarResultado(r)
}
function redondearArriba(){
    let { num2 } = obtenerValores()
    let r = Math.ceil(num2)
    mostrarResultado(r)
}
