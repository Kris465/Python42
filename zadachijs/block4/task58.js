const prompt = require('prompt-sync')();
const number = prompt("Введите трехзначное число:");

// Проверка на наличие цифр 4 или 7
const contains4or7 = number.includes('4') || number.includes('7');

// Проверка на наличие цифр 3, 6 или 9
const contains3or6or9 = number.includes('3') || number.includes('6') || number.includes('9');

// Вывод результатов
console.log(`Цифры 4 или 7 входят в число: ${contains4or7}`);
console.log(`Цифры 3, 6 или 9 входят в число: ${contains3or6or9}`);
