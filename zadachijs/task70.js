const prompt = require('prompt-sync')();
let a = prompt("Введите первое десятичное число: ");
let b = prompt("Введите второе десятичное число: ");

if (a != b) {
    console.log(`Число ${Math.max(a, b)} больше, чем ${Math.min(a, b)}`);
};
     
