//Registro de automóviles

//1.- Crear constructor con objeto automovil(marca,modelo,color,anio,titular)
function Automovil(marca,modelo,color,anio,titular){
    this.marca = marca;
    this.modelo = modelo;
    this.color = color;
    this.anio = anio;
    this.titular = titular;
}


//2.- Crear 3 instancias de automóviles
let auto1 = new Automovil("Nissan","Versa","Rojo","2003","Agencia")
let auto2 = new Automovil("Chevrolet","Sedán","Gris","2005","Agencia")
let auto3 = new Automovil("SEAT","Toledo","Negro","2015","Agencia")

//3.- Crear 3 métodos para el prototipo
//vender automovil(titular)
Automovil.prototype.vender = function(titular){
    this.titular = titular
    console.log("El coche de marca "+this.marca+" es propiedad de "+this.titular)
}
//ver auto string: marca modelo - anio - titular
Automovil.prototype.verAuto = function(){
    return this.marca+" "+this.modelo+" - "+this.anio+" - "+this.titular
}
//encender (alert(en marcha))
Automovil.prototype.encender = function(){
    alert("Automovil "+this.marca+" encendido")
}
//boton de ver registros funcion
let automoviles = [auto1,auto2,auto3]
function verRegistros(){
    //accedemos al elemento lista
    let lista = document.getElementById("registros")
    lista.innerHTML = ""
    let marcas = []
    let modelos = []
    let anios = []
    let string = "";
    for (let auto of automoviles){
        let li = document.createElement("li")
        li.textContent = auto.verAuto() //usamos función
        lista.appendChild(li) //agregamos elemento a la lista
    }
}
function encender(coche){
    //elementos
    let coche = document.getElementById("carro")
    if (coche != ""){
        coche.encender()
    }else{
        alert("Seleccionar coche")
    }
}
