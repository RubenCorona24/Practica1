//obtenemos los elementos html
let elementoNombre = document.getElementById("bancoNombre")
let elementoSucursal = document.getElementById("sucursal")
let elementoTitular = document.getElementById("titular")
let elementoNumero= document.getElementById("numCuenta")
let elementoSaldo = document.getElementById("saldo")
let elementoCbu = document.getElementById("cbu")
let elementoAbierto = document.getElementById("abierto")

//extraemos datos con fetch
fetch("datos.json")
.then(response=>response.json())
.then(data=> {
    elementoNombre.textContent = data.banco
    elementoSucursal.textContent = data.sucursal
    elementoTitular.textContent = data.titular
    elementoNumero.textContent = data.nro_cuenta
    for (let item of data.saldo) {
        let p = document.createElement("p")
        p.textContent = item.moneda + ": $" + item.monto
        elementoSaldo.appendChild(p)
}
    elementoCbu.textContent = data.cbu
    elementoAbierto.textContent = data.abierto
})