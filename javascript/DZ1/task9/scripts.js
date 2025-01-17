document.getElementById('Button').addEventListener('click', function() {
    const firstNum = parseInt(document.getElementById('numInput').value);
    const message = document.getElementById('message');

    if (firstNum) {
        let digit1 = Math.floor(firstNum / 100) ;
        let digit2 = Math.floor(firstNum / 10) % 10;
        let digit3 = firstNum % 10;
        message.textContent = `Вот перевёрнутое число ---> ${digit3}${digit2}${digit1}`;
    }else{
        message.textContent = 'Пожалуйста, не ломай мою программу, напиши просто трёхзначное число';
    }
})