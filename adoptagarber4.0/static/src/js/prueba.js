// document.addEventListener('DOMContentLoaded', function() {
//     if (window.location.href === 'http://192.168.100.85:8070/adopta-results') {
//         console.log('Hola mundo');
//     }
// });
// document.addEventListener('DOMContentLoaded', function(){
//     boton = document.getElementById("action_view_pet");
//     boton.addEventListener("click", function(){
//         window.location.href = "http://192.168.100.85:8070/adopta-results";
//         console.log("El boton funciona");
//     });
// });
document.addEventListener('DOMContentLoaded', function() {
    const cardsClickable = document.querySelectorAll(".card-clickable");

    cardsClickable.forEach((card) => {
        card.addEventListener("click", () => {
            const mascotaId = card.getAttribute('data-mascota-id');
            const url = `/adopta/${mascotaId}`;
            window.location.href = url;
        });
    });
});
