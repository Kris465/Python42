const prompt = require('prompt-sync')();
const n = prompt("Введите значение n (100 ≤ n ≤ 999): ");

let g = n[0] + n[2] + n[1];

console.log(g);

