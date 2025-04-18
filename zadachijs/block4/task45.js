const prompt = require('prompt-sync')();
let a = parseFloat(prompt('Введите A: '));
let b = parseFloat(prompt('Введите B: '));
let c = parseFloat(prompt('Введите C: '));

function hasEqualPair(a, b, c) {
    return a === b || a === c || b === c;
}

if (hasEqualPair(a, b, c)) {
    console.log("Среди чисел есть хотя бы одна пара равных.");
} else {
    console.log("Все числа различны.");
}
