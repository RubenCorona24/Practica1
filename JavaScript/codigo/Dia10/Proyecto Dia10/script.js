//creamos constructores 

class Animal{
    constructor(nombre,peso,edad){
        this.nombre = nombre;
        this.peso =peso;
        this.edad = edad;
    }
}

//subclase Perro
class Perro extends Animal{
    constructor(nombre,peso,edad,raza){
        super(nombre,peso,edad);
        this.raza = raza
    }
}

//subclase Gato
class Gato extends Animal{
    constructor(nombre,peso,edad,sexo){
        super(nombre,peso,edad);
        this.sexo = sexo
    }
}

//subclase Conejo
class Conejo extends Animal{
    constructor(nombre,peso,edad,color){
        super(nombre,peso,edad);
        this.color = color
    }
}

//metodo informacion
Animal.prototype.informacion = function(){
    return "Nombre del animal: "+this.nombre+" Peso: "+this.peso+" Edad: "+this.edad
}

//creamos 3 instancias

let perro = new Perro("Crispin","28kg","12 años","Cruza")
let gato = new Gato("Kati","18kg","9 años","Femenino")
let conejo = new Conejo("Juari","6 kg","3 años","Marrón")

animales = [perro,gato,conejo]
function mostrarAnimales(){
    let contenedorPerro = document.getElementById("contenedorPerro")
    let contenedorGato = document.getElementById("contenedorGato")
    let contenedorConejo = document.getElementById("contenedorConejo")
    //extraemos listas
    let listaPerro = document.getElementById("listaPerro")
    let listaGato = document.getElementById("listaGato")
    let listaConejo = document.getElementById("listaConejo")
    contenedorPerro.innerHTML = ""
    contenedorGato.innerHTML = ""
    contenedorConejo.innerHTML = ""
    listaPerro.innerHTML = ""
    listaGato.innerHTML = ""
    listaConejo.innerHTML = ""
    for (let animal of animales){
        if (animal instanceof Perro){
            let elementoimagen = document.createElement("img")
            elementoimagen.setAttribute("src","perro.jpg")
            contenedorPerro.appendChild(elementoimagen)
            let liPrincipal = document.createElement("li")
            liPrincipal.textContent = "Perro"
            listaPerro.appendChild(liPrincipal)
            for (let item in animal){
                let li = document.createElement("li")
                li.textContent = item+": "+animal[item]
                listaPerro.appendChild(li)
            }  
        contenedorPerro.appendChild(listaPerro)
        }else if (animal instanceof Gato){
            let elementoimagen = document.createElement("img")
            elementoimagen.setAttribute("src","gato.jpg")
            contenedorGato.appendChild(elementoimagen)
            let liPrincipal = document.createElement("li")
            liPrincipal.textContent = "Gato"
            listaGato.appendChild(liPrincipal)
            for (let item in animal){
                let li = document.createElement("li")
                li.textContent = item+": "+animal[item]
                listaGato.appendChild(li)
            }
        contenedorGato.appendChild(listaGato)
        }else if (animal instanceof Conejo){
            let elementoimagen = document.createElement("img")
            elementoimagen.setAttribute("src","conejo.jpg")
            contenedorConejo.appendChild(elementoimagen)
            let liPrincipal = document.createElement("li")
            liPrincipal.textContent = "Conejo"
            listaConejo.appendChild(liPrincipal)
            for (let item in animal){
                let li = document.createElement("li")
                li.textContent = item+": "+animal[item]
                listaConejo.appendChild(li)
            }
        contenedorConejo.appendChild(listaConejo)
        }
    }
    alert("Información Mostrada de animales ✅ ")
} 
function resetearInfo(){
    // limpiar solo las listas e imágenes, no los contenedores
    let listaPerro = document.getElementById("listaPerro")
    let listaGato = document.getElementById("listaGato")
    let listaConejo = document.getElementById("listaConejo")

    listaPerro.innerHTML = ""
    listaGato.innerHTML = ""
    listaConejo.innerHTML = ""

    // quitar imágenes
    let imagenes = document.querySelectorAll("img")
    imagenes.forEach(img => img.remove())

    alert("Información Reseteada ✅")
}