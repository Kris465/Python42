const prompt = require('prompt-sync')();
let n = prompt("Введите n год: ");

if (n / 4) {
    console.log("Год високосный.");
} else if (n / 100 || n / 400) {
    console.log("Год високосный");
} else {
    console.log("Год не високосный");
}
