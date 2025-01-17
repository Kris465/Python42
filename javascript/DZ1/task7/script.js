document.getElementById('Button').addEventListener('click', function() {
    const flashcard_GB = parseFloat(document.getElementById('GB').value);
    

    if (!isNaN(flashcard_GB) && flashcard_GB > 0) {
        const files = flashcard_GB * 1024 / 820;
        document.getElementById('result').innerText = `Колличество файлов ${files.toFixed(2)}`;

    } else{
        document.getElementById('result').innerText = 'Пожалуйста, введите нормально...';
    }
});