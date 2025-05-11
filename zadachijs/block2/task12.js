// Дано трехзначное число. Найти: 
// а) число единиц в нем; 
// б) число десятков в нем; 
// в) сумму его цифр; 
// г) произведение его цифр.

const prompt = require("prompt-sync")();
const a = prompt("напишите число: ")

if (a < 100 || a > 999) {
    return "Ошибка: число должно быть трехзначным (100-999)";
  }

let edinici = a % 10;
let dec = Math.floor((a % 100) / 10);
let hun = Math.floor(a / 100);
let sum = edinici + dec + hun;
let pro = edinici * dec * hun;

console.log(f`единицы: ${edinici}`)
console.log(f`десятки: ${dec}`)
console.log(f`десятки: ${hun}`)
console.log(f`сумма числа: ${sum}`)
console.log(f`произведение числа: ${pro}`)
