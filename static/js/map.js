// Инициализация карты
const map = L.map('map').setView([51.768, 55.097], 7); // Центр на Оренбургской области

// Добавление слоя с картой
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Загрузка данных о погибших
fetch('/api/memorials')
    .then(response => response.json())
    .then(data => {
        data.forEach(memorial => {
            if (memorial.latitude && memorial.longitude) {
                const marker = L.marker([memorial.latitude, memorial.longitude]).addTo(map);
                marker.bindPopup(`
                    <b>${memorial.last_name} ${memorial.first_name}</b><br>
                    ${memorial.birth_place}<br>
                    ${memorial.death_date}
                `);
            }
        });
    });

let element = document.querySelector('.leaflet-control-attribution');
if (element) {
  element.remove();
}