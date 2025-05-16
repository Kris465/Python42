const prompt = require('prompt-sync')();
let mass = [1, 10, 100, 200, 223, 500, 88, 345, 456, 888, 1000];
let s = prompt("Введите число (0-9): ");
let k = prompt("Введите второе число (0-9): ");

let sINmass = mass[s];
let kINmass = mass[k];

if (sINmass >= 0) {
    console.log(`Число под номером ${s} является положительным.`)
} else {
    console.log(`Число под номером ${s} является отрицательным.`)
};

if (kINmass % 2 == 0) {
    console.log(`Число под номер ${k} чётное.`)
} else {
    console.log(`Число под номером ${k} не чётное.`)
};

if (sINmass > kINmass) {
    console.log(`Число под номером ${s} больше чем число под номером ${k}.`)
} else {
    console.log(`Число под номером ${k} больше чем число под номером ${s}.`)
};