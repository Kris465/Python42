const prompt = require('prompt-sync')();
let x = prompt("Введите двузначное число: ");
let num1 = Math.floor(x / 10)
let num2 = x % 10

//вариант 1

// if (num1 == 4 || num2 == 4) {
//     console.log("Цифры 4 входят ");
// } else if (num1 == 7 || num2 == 7) {
//     console.log("Цифры 7 входят");
// } else {
//     console.log("Цифры 4 или 7 не входят");
// }

//вариант 2
if (num1 == 3 || num2 == 3) {
    console.log("Цифры 3 входят ");
} else if (num1 == 6 || num2 == 6) {
    console.log("Цифры 6 входят");L
} else if (num1 == 9 || num2 == 9) {
    console.log("Цифры 9 входят");
} else {
    console.log("Цифры 3, 6, 9 - не входят");
}
