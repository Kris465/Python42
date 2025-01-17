document.getElementById('Button').addEventListener('click', function() {
    const distance = parseFloat(document.getElementById('distance').value);
    const time = parseFloat(document.getElementById('time').value);

    if (!isNaN(distance) && distance > 0 && !isNaN(time) && time > 0) {
        const speed = distance / time;
        document.getElementById('result').innerText = `Скорость: ${speed.toFixed(2)} км/ч`;

    } else{
        document.getElementById('result').innerText = 'Пожалуйста, введите нормально...';
    }
});