$(document).ready(function(){
    $("button") //selecciona todos los elementos button
    .click(function(){
        let valorInput = $("input").val();
        alert("El input dice: "+valorInput)
    })
})