// Intento solucionar esto cuando vuelva jeje
function updateImage(imageField, imagePathField)
 {
    var imagePath = imagePathField.value;
    
    if (imagePath) {
        imageField.src = imagePath;
    } else {
        imageField.src = "";
    }
}

document.addEventListener("DOMContentLoaded", function() 
{
    var imageField = document.querySelector("[name='image']");
    var imagePathField = document.querySelector("[name='image_path']");

    if (imagePathField && imageField) {
        // Actualizar la imagen al cargar la página
        updateImage(imageField, imagePathField);

        // Escuchar cambios en el campo de ruta de imagen y actualizar la imagen en consecuencia
        imagePathField.addEventListener("input", function() {
            updateImage(imageField, imagePathField);
        });
    }
});