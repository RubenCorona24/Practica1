let selector = document.getElementById("selector");

let lista = document.getElementById("listaProductos");

selector.addEventListener("change", function(e) {

    lista.innerHTML = "";

    let categoria = e.target.value;

    fetch("datos.json")
    .then(response => response.json())
    .then(data => {

        for (let producto of data.data) {

            if (producto.categoria === categoria) {

                let li = document.createElement("li");
                li.textContent = producto.nombre;
                let precio = document.createElement("p")
                precio.textContent = `Precio: $${producto.precio}`
                let p = document.createElement("p");
                p.textContent = producto.descripcion;

                // ocultar descripción inicialmente
                p.style.display = "none";

                lista.appendChild(li);
                lista.appendChild(precio)
                lista.appendChild(p);

                // hover SOBRE el li
                li.addEventListener("mouseover", function() {
                    p.style.display = "block";
                });

                li.addEventListener("mouseout", function() {
                    p.style.display = "none";
                });

            }

        }

    });

});