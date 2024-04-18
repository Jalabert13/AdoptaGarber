document.addEventListener("DOMContentLoaded", function () {
    // Obtener todas las imágenes miniatura
    var miniImages = document.querySelectorAll(".mini-image");
    var fullscreenImgContainer = document.querySelector(".fullscreen-img");
    var fullscreenImg = document.getElementById("fullscreen-image");
    var prueba = document.getElementById("ofw3gkjet5nt");
    // Agregar evento de clic a cada imagen miniatura
    miniImages.forEach(function (miniImage) {
        miniImage.addEventListener("click", function () {
            // Mostrar la imagen en pantalla completa
            fullscreenImg.src = this.src;
            fullscreenImgContainer.style.display = "flex";
        });
    });

    // Ocultar la imagen en pantalla completa al hacer clic en ella
    fullscreenImgContainer.addEventListener("click", function () {
        this.style.display = "none";
    });
});
