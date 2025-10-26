async function fetchMoisture() {
    try {
        const response = await fetch('/moisture');
        const data = await response.json();
        const display = document.getElementById('moisture-value');

        if (data.moisture === 'Veri yok') {
            display.textContent = "Henüz veri alınmadı";
        } else {
            display.textContent = data.moisture;
        }
    } catch (error) {
        console.error('Hata:', error);
        document.getElementById('moisture-value').textContent = "Veri alınırken hata oluştu.";
    }
}

// Sayfa yüklendiğinde ve her 5 saniyede bir veriyi yenile
fetchMoisture();
setInterval(fetchMoisture, 5000);
