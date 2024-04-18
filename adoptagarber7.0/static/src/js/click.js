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
