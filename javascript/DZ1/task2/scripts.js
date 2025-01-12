document.getElementById('Button').addEventListener('click', function() {
    const year = document.getElementById('nameInput').value;
    

    if (year) {
        message.textContent = `Вам, ${2025 - year}!`;
    } else {
        message.textContent = 'Пожалуйста, введите свое имя!';
    }

});