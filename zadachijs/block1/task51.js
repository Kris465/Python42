let prompt = require('prompt-sync')();
let a = prompt("Введите хз1 ");
let b = prompt("Введите хз2 ");
let c = prompt("Введите хз3 ");
let d = prompt("Введите хз4 ");
if ((a - 1) * (b - 1) == c * d) {
    console.log("Поздравляю, открытка поместится");
} else{
    console.log("пОЗДРАВЛЯЮ, открытка не поместится");
}
