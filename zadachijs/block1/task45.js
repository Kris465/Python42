// Даны два числа. Найти их сумму, разность, произведение, а также частное от 
// деления первого числа на второе. 


const prompt = require('prompt-sync')();
const x = Number(prompt('Введите число "x": '));
const y = Number(prompt('Введите число "y": '));
const sum = x + y;
const minus = x - y;
const proizvedenie = x * y;
const chastnoe = x / y;

console.log(sum);
console.log(minus);
console.log(proizvedenie);
console.log(chastnoe);
