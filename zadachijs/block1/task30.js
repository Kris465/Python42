let prompt = require('prompt-sync')();

let x = parseInt(prompt("Введите x "));
let y = parseInt(prompt("Введите y "));
console.log(`z = ${x ** 3 - 2.5 * x * y + 1.78 * x ** 2 - 2.5 * y + 1}`)
