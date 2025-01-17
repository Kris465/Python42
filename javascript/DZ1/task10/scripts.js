document.getElementById('Button').addEventListener('click', function() {
    // const name = prompt("Введите свое имя: ")
    const number = document.getElementById('nameInput').value;
    const message = document.getElementById('message');

    if (number % 2 == 0) {
        alert("четное");
        message.textContent = "Правильно";
    } else {
        alert('нечетное')
        message.textContent = 'Введите четное число!!!!!';
    }
});