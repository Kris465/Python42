const prompt = require('prompt-sync')();
let a = parseFloat(prompt('Введите A: '));
let b = parseFloat(prompt('Введите B: '));
let c = parseFloat(prompt('Введите C: '));

if (a===0) {
    console.log("a не равно 0")
    return
}

const discriminant = b * b - 4 * a * c 

if (discriminant > 0) {
const x1 = (-b + Math.sqrt(discriminant)) / (2 * a)
const x2 = (+b + Math.sqrt(discriminant)) / (2 * a)
console.log("имеет два корня")
}
if(discriminant===0) {
const x = -b / (2 * a)
console.log("Имеет один корень")
}

