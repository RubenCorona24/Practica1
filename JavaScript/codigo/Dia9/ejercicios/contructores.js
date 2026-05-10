// Constructores básicos

function Animal(nombre,especie,edad){
    this.nombre = nombre;
    this.especie = especie;
    this.edad = edad;
}
Animal.prototype.presentarse = function(){
    console.log("Soy "+this.nombre+", soy un "+this.especie+" y tengo "+this.edad+" años")
}

//creamos instancias
let animal1 = Animal("Crispin","Perro","2")

function Producto(nombre,precio,descuento){
    this.nombre = nombre;
    this.precio = precio;
    this.descuento = descuento;
}
Producto.prototype.precioFinal = function(){
    let descontado = parseFloat(this.precio/this.descuento)
    let precioFinal = parseFloat(this.precio - this.descontado)
    console.log("Precio con descuento: "+precioFinal)
}

//Constructores avanzados

function Alumno(nombre,grado,calificaciones){
    this.nombre = nombre;
    this.grado = grado;
    this.calificaciones = calificaciones;
}
Alumno.prototype.promedio = function(){
    let sumatoria = 0;
    for (calif of this.calificaciones){
        sumatoria = sumatoria + calif
    }
    let promedio = sumatoria/this.calificaciones.length
    console.log("Promedio de "+this.nombre+": "+promedio)
}
Alumno.prototype.aprobo = function(){
    let sumatoria = 0;
    for (calif of this.calificaciones){
        sumatoria = sumatoria + calif
    }
    let promedio = sumatoria/this.calificaciones.length
    if (promedio>=6){
        return "Aprobado"
    }else{
        return "No aprobado"
    }
}
Alumno.prototype.mejorNota = function(){
    let mejorNota = this.calificaciones[0];
    for (nota of this.calificaciones){
        if (nota>mejorNota){
            mejorNota = nota
        }
    }
    console.log("Mejor nota: "+mejorNota)
}


//Reto final: Sistema de Hospital

function Paciente(nombre, edad, enfermedad, activo) {
    this.nombre = nombre
    this.edad = edad
    this.enfermedad = enfermedad
    this.activo = activo
}

function Hospital(nombre) {
    this.nombre = nombre
    this.pacientes = []  // ✅ array vacío por defecto
}

Hospital.prototype.ingresarPaciente = function(paciente) {
    this.pacientes.push(paciente)
    console.log("✅ Paciente " + paciente.nombre + " agregado")
}

Hospital.prototype.darDeAlta = function(nombre) {
    let encontrado = false
    for (let paciente of this.pacientes) {
        if (paciente.nombre == nombre) {  // ✅ comparar .nombre
            paciente.activo = false
            encontrado = true
            console.log("✅ Paciente " + nombre + " dado de alta")
        }
    }
    if (!encontrado) console.log("⚠️ Paciente no encontrado")
}

Hospital.prototype.pacientesActivos = function() {
    let totalActivos = 0
    for (let paciente of this.pacientes) {
        if (paciente.activo === true) {
            totalActivos++  // ✅ incremento correcto
        }
    }
    console.log("🏥 Pacientes activos: " + totalActivos)
}

Hospital.prototype.buscarPaciente = function(nombre) {
    for (let paciente of this.pacientes) {
        if (paciente.nombre == nombre) {
            for (let item in paciente) {
                if (typeof paciente[item] !== "function") {
                    console.log(item + ": " + paciente[item])
                }
            }
        }
    }
}
let hospital = new Hospital("Buena Ventura")

function nuevoPaciente(){
    let contenedor = document.getElementById("contenedor")
    contenedor.innerHTML = ""
    let labelPaciente = document.createElement("label")
    labelPaciente.innerText = "Nombre del Paciente  "
    labelPaciente.setAttribute("for","paciente")
    let inputPaciente = document.createElement("input")
    let inputEdad = document.createElement("input")
    inputEdad.setAttribute("id","edad")
    inputPaciente.setAttribute("id","paciente")
    let labelEdad = document.createElement("label")
    labelEdad.innerText = "  Edad  "
    labelEdad.setAttribute("for","edad")
    let inputEnfermedad = document.createElement("input")
    inputEnfermedad.setAttribute("id","enfermedad")
    let labelEnfermedad = document.createElement("label")
    labelEnfermedad.innerText = "  Enfermedad  "
    labelEnfermedad.setAttribute("for","enfermedad")
    //ingresar input y label a contenedor 
    let espacio= document.createElement("br")
    contenedor.appendChild(espacio)
    contenedor.appendChild(labelPaciente)
    contenedor.appendChild(inputPaciente)
    contenedor.appendChild(labelEdad)
    contenedor.appendChild(inputEdad)
    contenedor.appendChild(labelEnfermedad)
    contenedor.appendChild(inputEnfermedad)
    //boton ingresar
    let buttonIngresar = document.createElement("button")
    buttonIngresar.setAttribute("onclick","ingresar()")
    buttonIngresar.textContent = "Ingresar Paciente"
    contenedor.appendChild(buttonIngresar)
}   
pacientes = []

function ingresar(){
    let nombre = document.getElementById("paciente").value.trim()  // ✅ lee aquí
    let edad = document.getElementById("edad").value.trim()
    let enfermedad = document.getElementById("enfermedad").value.trim()
    if (!nombre || !edad || !enfermedad) {
        alert("⚠️ Llena todos los campos")
        return
    }
    let new_paciente = new Paciente(nombre,edad,enfermedad)
    pacientes.push(new_paciente)
    alert("Paciente ingresado con éxito ✅")

}

function verPacientes(){
    let elementoLista = document.getElementById("listaPacientes")
    elementoLista.innerHTML = ""
    
    if (pacientes.length === 0) {
        elementoLista.innerHTML = "<li>No hay pacientes registrados</li>"
        return
    }

    for (let paciente of pacientes) {  // ✅ let en el loop
        let elementoLi = document.createElement("li")
        elementoLi.textContent = paciente.nombre + " | Edad: " + paciente.edad + " | " + paciente.enfermedad
        elementoLista.appendChild(elementoLi)
    }
}