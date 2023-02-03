var coordinates = document.getElementById("coordinates");


function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.watchPosition(showPosition);
    } else { 
        coordinates.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    coordinates.innerHTML= position.coords.latitude + 
    ","+ position.coords.longitude;
    
    
}

