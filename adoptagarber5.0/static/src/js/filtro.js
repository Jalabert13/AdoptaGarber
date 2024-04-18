
// Seleccionar el elemento HTML que contiene el texto que deseas copiar
var elemento = document.getElementById("miElemento");

// Agregar un evento de clic al elemento
elemento.addEventListener("click", function() {
    // Obtener el texto del elemento
    var texto = elemento.textContent;

    // Utilizar la API navigator.clipboard para copiar el texto al portapapeles
    navigator.clipboard.writeText(texto).then(function() {
        console.log("Texto copiado al portapapeles: " + texto);
    }, function(err) {
        console.error("Error al copiar texto: ", err);
    });
});
