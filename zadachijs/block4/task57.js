const prompt = require('prompt-sync')();
let x = prompt("Введите первое число число: ");
let n = prompt("Введите n число число: ");
let num1 = Math.floor(x / 10)
let num2 = x % 10


//вариант 2
if (num1 == 6 || num2 == 6) {
    console.log("Цифры 6 входят ");
} else if (num1 == n || num2 == n) {
    console.log("Цифры n входят");
} else {
    console.log("Цифры не входят");
}























// let k = prompt("Введите третье  число: ");
// let n = prompt("Введите n  число: ");
// if (x == 6 && y == 6 && k == 6) {
//     console.log(`${str(x + y + k)} имеет число 6`); 
// } else if ( x == n && y == n && k == n) {
//     console.log(`${str(x + y + k)} имеет число n`); 
// } else {
//     console.log("ничего не получиться");
// }