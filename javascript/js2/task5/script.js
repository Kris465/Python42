document.getElementById('num').addEventListener('click', function(){

let year = prompt("Введите год:");

// Проверка, является ли введенное значение числом
year = Number(year);
if (isNaN(year) || year < 1) {
    alert("Пожалуйста, введите корректный год.");
    return;
}

// Проверка на високосный год (year % 400 === 0) || (year % 4 === 0 && year % 100 !== 0)
let isLeap = (year);

if (isLeap >= 1 && isLeap <= 100) {
    alert("это число от 1 до 100");
} else if (isLeap >= 101 && isLeap <= 200) {
    alert("это число от 101 до 200");
} else if (isLeap >= 201 && isLeap <= 300) {
    alert("это число от 201 до 300");
} else {
    alert("слишком много цифр");
}

});
