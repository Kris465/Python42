let prompt = require('prompt-sync')();
let a = prompt("Введите ширину  ");
let b = prompt("Введите длину ");
let c = prompt("Введите ширину открытки ");
let d = prompt("Введите длину открытки ");
if ((a - 1) * (b - 1) == c * d) {
    console.log("Поздравляю, открытка поместится");
} else{
    console.log("пОЗДРАВЛЯЮ, открытка не поместится");
}
