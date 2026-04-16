let elementoEdad = document.getElementById("edad")

function recomendar(genero){
    let textoPelicula = document.getElementById("textoPelicula")
    let edad = parseInt(elementoEdad.value);
    switch(genero){
        case "comedia":
            if (edad<13){
                textoPelicula.textContent = "Mi pobre Angelito"
            }else if (edad <16){
                textoPelicula.textContent = "Volver al futuro"
            }else{
                textoPelicula.textContent = "¿Qué pasó ayer?"
            }
            break;
        case "drama":
            if (edad<13){
                textoPelicula.textContent = "El Gigante de hierro"
            }else if (edad <16){
                textoPelicula.textContent = "Violet y Finch"
            }else{
                textoPelicula.textContent = "After"
            }
            break;
        case "musical":
            if (edad<13){
                textoPelicula.textContent = "Happy Feet: El pinguino"
            }else if (edad <16){
                textoPelicula.textContent = "Sing"
            }else{
                textoPelicula.textContent = "Coco"
            }
            break;
        case "crimen":
            if (edad<13){
                textoPelicula.textContent = "Una pareja explosiva"
            }else if (edad <16){
                textoPelicula.textContent = "Red Notice"
            }else{
                textoPelicula.textContent = "Venganza Implacable"
            }
            break;
    }
}

