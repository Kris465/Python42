const prompt = require('prompt-sync')();
const number = prompt("Введите четырехзначное число:");
const b = prompt("Введите некую цифру b: ")

const contains4 = number.includes('4');

const containsb = number.includes(`${b}`);

console.log(`Цифра 4 входит в число: ${contains4}`);
console.log(`Цифра ${b} входит в число: ${containsb}`);
