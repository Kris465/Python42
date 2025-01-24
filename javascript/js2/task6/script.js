document.addEventListener('DOMContentLoaded', function() {

    let number = prompt('Введите цифру:');

    if (number >= 0 && number <= 9){
        if (number == 0){
            alert('Ноль');
        }
        if (number == 1){
            alert('Один');
        }
        if (number == 2){
            alert('Два');
        }
        if (number == 3){
            alert('Три');
        }
        if (number == 4){
            alert('Четыре');
        }
        if (number == 5){
            alert('Пять');
        }
        if (number == 6){
            alert('Шесть');
        }
        if (number == 7){
            alert('Семь');
        }
        if (number == 8){
            alert('Восемь');
        }
        if (number == 9){
            alert('Девять');
        }
            
    } else {
        alert('Не цифра');
    }

});