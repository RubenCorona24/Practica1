//creamos objetos: Persona y Auto
function Persona(name,age,city){
    this.name = name;
    this.age = age;
    this.city = city;
    this.greet = function presentarse(){
        console.log("Hola, me llamo "+this.name+", tengo "+this.age+" años y vivo en "+this.city)
    }
}

//creamos instancias de persona
let user1 = new Persona("Ruben",18,"Nicolás Romero")
let user2 = new Persona("Juan",22,"New York")
user1.greet()

//Nivel 2: Constructor Producto con: nombre,precio,cantidad, agregar método totalInventario()

function Producto(nombre,precio,cantidad){
    this.nombre = nombre;
    this.precio = precio;
    this.cantidad = cantidad
    //agregamos método
    this.totalInventario = function totalInventario(){
        let inventario = parseInt(this.precio * this.cantidad)
        console.log("Inventario: "+inventario)
    }
}

//creamos instancias
let producto1 = new Producto("Camisa",120,12)
let producto2 = new Producto("Pantalón",129,11)
let producto3 = new Producto("Jabon",189,3)

producto1.totalInventario()


//Constructor de estudiantes: nombre,carrera,calificaciones(array),método promedio
function Estudiante(nombre,carrera,calificaciones){
    this.nombre = nombre;
    this.carrera = carrera;
    this.calificaciones = calificaciones;
    this.promedio = function promedio(){
        let conteo = 0
        for (let c of this.calificaciones){
            conteo = conteo + c
        }
        let promedio = conteo/this.calificaciones.length
        console.log("Promedio General: "+promedio)
    }
}

let est1 = new Estudiante("Carlos","Finanzas",[9,9,10,12,11])
est1.promedio()

//  Nivel 2: For in
//recorrer objeto con for in
let telefono = {
    marca: "Samsung",
    modelo: "S23",
    precio: 15000,
    color: "Negro"
}
function iterar(objeto){
    for (item in objeto){
        console.log(item+": "+objeto[item])
    }
}

iterar(telefono)
//Nivel3: Inventario de tiend
//Constructor Tienda: nombre, productos (array de objetos). Agrega métodos: totalProductos()
function Tienda(nombre,productos,precio){
    this.nombre = nombre;
    this.productos = productos;
    this.precio = precio
    this.totalProductos = function totalProductos(){
        let conteo = 0
        for (producto in productos){
            conteo = conteo + 1
        }
        console.log("Total Productos: "+conteo)
    }

}
let tienda1 = new Tienda("Productos RSC",['Manzana','Shampoo','Platanos','Cosméticos'],[12,23,34,34])
tienda1.totalProductos()

//Sistema de empleados
function Empleado(nombre,puesto,salario){
    this.nombre = nombre;
    this.puesto = puesto;
    this.salario = salario;
    this.info = function informacion(){
        console.log("Nombre: "+this.nombre+" Puesto: "+this.puesto+" Salario: "+this.salario)
    }
}
//instancias
let empl1 = new Empleado("Jordan","Ciberseguridad",1400)
let empl2 = new Empleado("Jonathan","Gerente",23900)
let empl3 = new Empleado("Giovanni","Ciberseguridad",1600)
let empl4 = new Empleado("Lucy","Ciberseguridad",1200)
let empl5 = new Empleado("Erika","Ciberseguridad",850)

let empleados = [empl1,empl2,empl3,empl4,empl5]
function mayorSalario(){
    let mayorSalario = empleados[0]
    for (let empleado of empleados){
        if (empleado.salario > mayorSalario.salario){
            mayorSalario = empleado
        } 
    }
    console.log("El mayor salario es de: "+mayorSalario.nombre+" con $"+mayorSalario.salario)
}
function menorSalario(){
    let menorSalario = empleados[0]
    for (let empleado of empleados){
        if (empleado.salario <menorSalario.salario){
            menorSalario = empleado
        } 
    }
    console.log("El menor salario es de: "+menorSalario.nombre+" con $"+menorSalario.salario)
}
mayorSalario()
menorSalario()