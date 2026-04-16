let elementoPrecio = document.getElementById("textoPrecio")
let elementoFruta = document.getElementById("numFruta")
function consultarPrecio(){
     let fruta = elementoFruta.value;
     //empezamos el switch
     switch (fruta)
     {
        case "1":
            elementoPrecio.textContent = "Precio Banana: $23.8";
            break; //Siempre terminar con break
        case "2":
            elementoPrecio.textContent = "Precio Manzana: $18.4";
            break; //Siempre terminar con break
        case "3":
            elementoPrecio.textContent = "Precio Uvas: $32.6";
            break;
        case "4":
            elementoPrecio.textContent = "Precio Naranja: $17.3";
            break;
        case "5":
            elementoPrecio.textContent = "Precio Sandía: $34.9";
            break;
     }
}