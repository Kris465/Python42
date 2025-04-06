const prompt = require('prompt-sync')();
let a = prompt("Введите первое десятичное число: ");
let b = prompt("Введите второе десятичное число: ");

// Вариант 1
// if (a > b) {
//     console.log(`Число ${a} больше, чем ${b}`);
// };
// if (a < b) {
//     console.log(`Число ${b} больше, чем ${a}`);
// };

// Вариант 2
if (a != b) {
    console.log(`Число ${Math.max(a, b)} больше, чем ${Math.min(a, b)}`);
};