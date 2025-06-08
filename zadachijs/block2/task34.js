let prompt = require('prompt-sync')();
let a1 = prompt("Введите a1 ");
let a2 = prompt("Введите a2 ");
let b = prompt("Введите b ");
let c = a1 + b
if (a1 + b <= 9) {
 console.log(`${toString(a1 + c)}`);
} else {
    console.log("не получится");
}