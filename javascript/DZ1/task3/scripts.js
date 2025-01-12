document.getElementById('Button').addEventListener('click', function() {
    const sid = document.getElementById('nameInput').value;
    const message = document.getElementById('message');

    if (sid) {
        message.textContent = `ваше значени, ${sid*4}!`;
    } else {
        message.textContent = 'Пожалуйста, введите свое имя!';
    }

});