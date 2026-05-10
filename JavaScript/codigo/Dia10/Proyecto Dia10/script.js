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
    alert("Nombre del animal: "+this.nombre+" Peso: "+this.peso+" Edad: "+this.edad)
}

//creamos 3 instancias

let perro = new Perro("Crispin","28kg","12 años","Cruza")
let gato = new Gato("Kati","18kg","9 años","Femenino")
let conejo = new Conejo("Juari","6 kg","3 años","Marrón")

animales = [perro,gato,conejo]
function mostrarAnimales(){
    let contenedorPerro = document.getElementById("contenedorPerro")
    //extraemos listas
    let listaPerro = document.getElementById("listaPerro")
    let listaGato = document.getElementById("listaGato")
    let listaConejo = document.getElementById("listaConejo")
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
        
        }else if (animal instanceof Gato){
            let liPrincipal = document.createElement("li")
            liPrincipal.textContent = "Gato"
            listaGato.appendChild(liPrincipal)
            for (let item in animal){
                let li = document.createElement("li")
                li.textContent = item+": "+animal[item]
                listaGato.appendChild(li)
            }

        }else if (animal instanceof Conejo){
            let liPrincipal = document.createElement("li")
            liPrincipal.textContent = "Conejo"
            listaConejo.appendChild(liPrincipal)
            for (let item in animal){
                let li = document.createElement("li")
                li.textContent = item+": "+animal[item]
                listaConejo.appendChild(li)
            }
        }
    }
} 