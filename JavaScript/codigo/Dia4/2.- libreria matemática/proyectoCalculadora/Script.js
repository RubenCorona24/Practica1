let elementoResultado = document.getElementById("resultado")
let elementoNum1 = document.getElementById("num1")
let elementoNum2 = document.getElementById("num2")

// ═══════════════════════════════════════
// FUNCIONES AUXILIARES (reutilizables)
// ═══════════════════════════════════════

// Muestra el resultado en pantalla
function mostrarResultado(resultado) {
    elementoResultado.textContent = resultado
}

// Obtiene y convierte los valores de los inputs
function obtenerValores() {
    let num1 = parseFloat(elementoNum1.value)  // parseFloat para permitir decimales
    let num2 = parseFloat(elementoNum2.value)
    return { num1, num2 }
}

// Valida que los números no sean NaN
// ...numeros permite pasar 1 o 2 argumentos
function esValido(...numeros) {
    return numeros.every(n => !isNaN(n))
    // every() revisa que TODOS cumplan la condición
}

// ═══════════════════════════════════════
// OPERACIONES BÁSICAS (usan num1 y num2)
// ═══════════════════════════════════════

function sumar() {
    let { num1, num2 } = obtenerValores()
    if (!esValido(num1, num2)) {
        mostrarResultado("⚠️ Ingresa ambos valores")
        return
    }
    mostrarResultado(num1 + num2)
}

function restar() {
    let { num1, num2 } = obtenerValores()
    if (!esValido(num1, num2)) {
        mostrarResultado("⚠️ Ingresa ambos valores")
        return
    }
    mostrarResultado(num1 - num2)
}

function multiplicar() {
    let { num1, num2 } = obtenerValores()
    if (!esValido(num1, num2)) {
        mostrarResultado("⚠️ Ingresa ambos valores")
        return
    }
    mostrarResultado(num1 * num2)
}

function dividir() {
    let { num1, num2 } = obtenerValores()
    if (!esValido(num1, num2)) {
        mostrarResultado("⚠️ Ingresa ambos valores")
        return
    }
    if (num2 === 0) {
        mostrarResultado("❌ Error: no se puede dividir entre 0")
        return
    }
    mostrarResultado((num1 / num2).toFixed(2))
}

function sacarPotencia() {
    let { num1, num2 } = obtenerValores()
    if (!esValido(num1, num2)) {
        mostrarResultado("⚠️ Ingresa ambos valores")
        return
    }
    // Math.pow(base, exponente)
    mostrarResultado(Math.pow(num1, num2))
}

function sacarRandom() {
    let { num1, num2 } = obtenerValores()
    if (!esValido(num1, num2)) {
        mostrarResultado("⚠️ Ingresa ambos valores")
        return
    }
    if (num1 >= num2) {
        mostrarResultado("⚠️ El mínimo debe ser menor que el máximo")
        return
    }
    // Fórmula estándar de número aleatorio entre min y max inclusive
    let r = Math.floor(Math.random() * (num2 - num1 + 1)) + num1
    mostrarResultado(r)
}

// ═══════════════════════════════════════
// OPERACIONES DE UN SOLO NÚMERO (num2)
// ═══════════════════════════════════════

function sacarRaiz() {
    let { num2 } = obtenerValores()
    if (!esValido(num2)) {
        mostrarResultado("⚠️ Ingresa el segundo valor")
        return
    }
    if (num2 < 0) {
        mostrarResultado("❌ Error: no existe raíz de números negativos")
        return
    }
    mostrarResultado(Math.sqrt(num2).toFixed(4))
}

function sacarAbsoluto() {
    let { num2 } = obtenerValores()
    if (!esValido(num2)) {
        mostrarResultado("⚠️ Ingresa el segundo valor")
        return
    }
    // Math.abs convierte negativos a positivos: abs(-5) → 5
    mostrarResultado(Math.abs(num2))
}

function redondearNumero() {
    let { num2 } = obtenerValores()
    if (!esValido(num2)) {
        mostrarResultado("⚠️ Ingresa el segundo valor")
        return
    }
    // Round: .4 hacia abajo, .5 hacia arriba
    mostrarResultado(Math.round(num2))
}

function redondearAlPiso() {
    let { num2 } = obtenerValores()
    if (!esValido(num2)) {
        mostrarResultado("⚠️ Ingresa el segundo valor")
        return
    }
    // Floor: siempre hacia abajo → 3.9 = 3
    mostrarResultado(Math.floor(num2))
}

function redondearArriba() {
    let { num2 } = obtenerValores()
    if (!esValido(num2)) {
        mostrarResultado("⚠️ Ingresa el segundo valor")
        return
    }
    // Ceil: siempre hacia arriba → 3.1 = 4
    mostrarResultado(Math.ceil(num2))
}
function reiniciar(){
    mostrarResultado("---")
    elementoNum1.value = 0
    elementoNum2.value = 0
}