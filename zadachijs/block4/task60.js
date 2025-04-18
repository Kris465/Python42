const prompt = require('prompt-sync')();
const number = prompt("Введите четырехзначное число:");
const b = prompt("Введите какую-то цифру b: ")

const contains2or7 = number.includes('2') || number.includes('7');

const contains3or6or9 = number.includes('3') || number.includes('6') || number.includes('9');

// Вывод результатов
console.log(`Цифры 2 или 7 входят в число: ${contains2or7}`);
console.log(`Цифры 3, 6 или 9 входят в число: ${contains3or6or9}`);

console.log(`Цифра 2 входит в число: ${contains2}`);
console.log(`Цифра ${b} входит в число: ${containsb}`);
