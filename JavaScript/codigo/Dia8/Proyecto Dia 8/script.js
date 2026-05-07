//Registro de empleados
//1.- Hacer el constructor empleado
function Trabajador(legajo,nombre,apellido,fechaNacimiento,cargo){
    this.legajo = legajo;
    this.nombre = nombre;
    this.apellido = apellido;
    this.fechaNacimiento = fechaNacimiento;
    this.cargo = cargo
    this.informacion = function info(){
        console.log("Legajo: "+this.legajo+" Nombre: "+this.nombre+" Apellido: "+this.apellido+" Fecha Nacimiento: "+this.fechaNacimiento+" Cargo: "+this.cargo)
    }
}
//creamos array de empleados
let empleados = []

//Obtener elementos HTML
let elementoLegajo = document.getElementById("legajo")
let elementoNombre = document.getElementById("nombre")
let elementoApellido = document.getElementById("apellido")
let elementofechaNacimento = document.getElementById("fechaNacimiento")
let elementoCargo = document.getElementById("cargo")

function cargarEmpleado(){
    let empleado = new Trabajador(elementoLegajo.value,
        elementoNombre.value,elementoApellido.value,elementofechaNacimento.value,elementoCargo.value
    )
    alert("Empleado cargado con éxito")
    empleados.push(empleado)
}

function mostrarEmpleados(){
    let string = "";
    for (let empleado of empleados){
        for (let item in empleado){
            if (item == "informacion"){
                continue
            }
            string = string + item + ": "+ empleado[item] + "\n"
        }
    }
    alert(string)
}

function resetear(){
    elementoLegajo.value = ""
    elementoNombre.value = ""
    elementoApellido.value = ""
    elementofechaNacimento.value = ""
    elementoCargo.value = ""
    
}