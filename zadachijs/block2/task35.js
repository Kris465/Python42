const prompt = require('prompt-sync')();
let a2 = parseInt(prompt("Введите кол-во десятков первого числа: "));
let a1 = parseInt(prompt("Введите кол-во единиц первого числа: "));

let b2 = parseInt(prompt("Введите кол-во десятков второго числа: "));
let b1 = parseInt(prompt("Введите кол-во единиц второго числа: "));

let x2 = parseInt(a2 + b2);
let x1 = parseInt(a1 + b1);

if (x1 > 9) {
    x1 = x1 - 10;
    x2 = x2 + 1;

    console.log(`Кол-во десятков: ${x2}`);
    console.log(`Кол-во единиц: ${x1}`);
} else {
    console.log(`Кол-во десятков: ${x2}`);
    console.log(`Кол-во единиц: ${x1}`);
};