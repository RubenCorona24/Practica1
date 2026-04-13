let totalCuenta = document.getElementById("totalCuenta")
let porcentajePropina = document.getElementById("porcentajePropina")
let elementoPropina = document.getElementById("propina")
let elementoTotalPagar = document.getElementById("totalPagar")
function calcularPropina(){
    let cuenta = parseFloat(totalCuenta.value) 
    let porcentaje =  parseFloat(porcentajePropina.value)
    let totalPropina = cuenta * (porcentaje / 100) 
    let pagoTotal = totalPropina + cuenta
    elementoPropina.textContent = "$"+totalPropina.toFixed(2)
    elementoTotalPagar.textContent = "$"+pagoTotal.toFixed(2)
    }
function reiniciar(){
    totalCuenta.value = ""
    porcentajePropina.value = ""
    elementoPropina.textContent = "$00.00"
    }