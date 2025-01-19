document.addEventListener('DOMContentLoaded', function() {

    let number = prompt('Введите число:');

    if (number >= 0 && number <= 100){
        alert('Принадлежит');
    } else {
        alert('Не принадлежит');
    }

});