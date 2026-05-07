// Constructor con método en el prototipo
function Trabajador(legajo, nombre, apellido, fechaNacimiento, cargo) {
    this.legajo = parseInt(legajo);
    this.nombre = nombre;
    this.apellido = apellido;
    this.fechaNacimiento = fechaNacimiento;
    this.cargo = cargo;
}

Trabajador.prototype.informacion = function () {
    console.log(`Legajo: ${this.legajo} | ${this.nombre} ${this.apellido} | ${this.cargo}`);
};

let empleados = [];

// Referencias al DOM
const elementoLegajo = document.getElementById("legajo");
const elementoNombre = document.getElementById("nombre");
const elementoApellido = document.getElementById("apellido");
const elementoFechaNacimiento = document.getElementById("fechaNacimiento");
const elementoCargo = document.getElementById("cargo");

function cargarEmpleado() {
    const legajo = elementoLegajo.value.trim();
    const nombre = elementoNombre.value.trim();
    const apellido = elementoApellido.value.trim();
    const fecha = elementoFechaNacimiento.value;
    const cargo = elementoCargo.value.trim();

    // Validación básica
    if (!legajo || !nombre || !apellido || !fecha || !cargo) {
        alert("Por favor completá todos los campos.");
        return;
    }

    // Legajo único
    if (empleados.some(e => e.legajo === parseInt(legajo))) {
        alert("Ya existe un empleado con ese legajo.");
        return;
    }

    empleados.push(new Trabajador(legajo, nombre, apellido, fecha, cargo));
    alert("Empleado cargado con éxito.");
    resetear();
}

function mostrarEmpleados() {
    if (empleados.length === 0) {
        alert("No hay empleados registrados.");
        return;
    }

    let string = "";
    for (const empleado of empleados) {
        for (const [clave, valor] of Object.entries(empleado)) {
            string += `${clave}: ${valor}\n`;
        }
        string += "---\n";
    }
    alert(string);
}

function resetear() {
    elementoLegajo.value = "";
    elementoNombre.value = "";
    elementoApellido.value = "";
    elementoFechaNacimiento.value = "";
    elementoCargo.value = "";
}