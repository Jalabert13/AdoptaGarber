
    function initMap() {
        // Ubicación de la mascota (ejemplo)
        var mascotaLocation = { lat: -34.397, lng: 150.644 }; // Esto debería ser reemplazado con la ubicación real de la mascota
        
        // Opciones del mapa
        var mapOptions = {
            center: mascotaLocation,
            zoom: 8 // Puedes ajustar el nivel de zoom según tus necesidades
        };
        
        // Crear el mapa
        var map = new google.maps.Map(document.getElementById('map'), mapOptions);
        
        // Opcional: Agregar un marcador en la ubicación de la mascota
        var marker = new google.maps.Marker({
            position: mascotaLocation,
            map: map,
            title: 'Ubicación de la mascota'
        });
    }