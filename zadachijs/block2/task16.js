const prompt = require('prompt-sync')();
let mass = [169, 1, 52, 43, 87, 30, 64, 32, 506, 904, 10];
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