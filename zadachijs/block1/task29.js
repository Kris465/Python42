let prompt = require('prompt-sync')();

let r = parseInt(prompt("Введите радиус окружности: "));

console.log(`Длина окружности = ${(2 * Math.PI) * r}`);
console.log(`Площадь круга = ${Math.PI * (r ** 2)}`);