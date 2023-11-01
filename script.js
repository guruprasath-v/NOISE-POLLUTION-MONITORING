// Simulate sensor data retrieval
function refreshSensorData() {
    // Replace with actual data retrieval code
    const noiseLevel = Math.floor(Math.random() * 100);
    const status = getNoiseStatus(noiseLevel);

    document.getElementById('noise-level').innerText = noiseLevel + ' dB';
    document.getElementById('status').innerText = status;
}

// Determine noise status based on noise level
function getNoiseStatus(noiseLevel) {
    if (noiseLevel <= 55) {
        return 'Quiet';
    } else if (noiseLevel > 55 && noiseLevel < 85) {
        return 'Moderate';
    } else {
        return 'High';
    }
}

// Initial data refresh
refreshSensorData();
