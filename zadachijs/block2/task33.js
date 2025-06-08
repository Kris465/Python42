// Вроде так :Р

const prompt = require('prompt-sync')();
const n = prompt("Введите значение x (100 ≤ n ≤ 999): ");

let x = n[1] + n[0] + n[2];

console.log(x);
