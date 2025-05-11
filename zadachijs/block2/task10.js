const prompt = require("prompt-sync")();
const meme = prompt("напишите число: ")

if (meme < 10 || meme > 99) {
    return "Ошибка: число должно быть двузначным (10-99)";
  }


let one1 = Math.floor(meme / 10);
let one2 = meme % 10;
let two = one1 + one2
let three = one1 * one2

console.log(f`десятки: ${one1}`)
console.log(f`единицы: ${one2}`)
console.log(f`сумма числа: ${two}`)
console.log(f`произведение числа: ${three}`)
