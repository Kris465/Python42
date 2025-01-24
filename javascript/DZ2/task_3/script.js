document.getElementById('button').addEventListener('click', function(){


let number = prompt("Введите трехзначное число:");
    if ( number >= 1000) {
        alert("Пожалуйста, введите корректное трехзначное число.");
        return;
    }                                                                                                        

    const digits = number.split('');
    const hasDuplicates = new Set(digits).size < digits.length;

    if (hasDuplicates) {
        alert("В числе есть одинаковые цифры.");
    } else {
        alert("В числе нет одинаковых цифр.");
    }
})