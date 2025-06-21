// Initialize map centered on your preferred location
var map = L.map('map').setView([0, 0], 1.5);

// Add OpenStreetMap tiles
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);


// List of places we've been
const places = [
    { name: "Toronto, Canada", coords: [43.65107, -79.347015] },
    { name: "Vancouver, Canada", coords: [49.2827, -123.1207] },
    { name: "Manila, Philippines", coords: [14.5995, 120.9842] },
    { name: "Seoul, South Korea", coords: [37.5503, 126.9971]},
    { name: "Jakarta, Indonesia", coords: [6.1944, 106.8229]},
    { name: "Suva, Fiji", coords: [18.1266, 178.4399]},
    { name: "Singapore, Singapore", coords: [1.3521, 103.8198]},
    { name: "Kuala Lumpur, Malaysia", coords: [3.1499, 101.6945]},
    { name: "Hong Kong City, Hong Kong ", coords: [22.3193, 114.1694]},
];

// Add markers
places.forEach(place => {
    L.marker(place.coords)
     .addTo(map)
     .bindPopup(`<b>${place.name}</b>`);
});
