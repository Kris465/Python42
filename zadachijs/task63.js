const prompt = require('prompt-sync')();

function areAllDigitsDifferent(n) {
    const s = n.toString().padStart(4, '0'); 
    const uniqueDigits = new Set(s);           
    return uniqueDigits.size === 4;            
}


const input = prompt("Введите натуральное число (n ≤ 9999): ");
const number = parseInt(input, 10);

if (isNaN(number)) {
    console.log("Ошибка: введите число!");
} else {
    const result = areAllDigitsDifferent(number);
    console.log(result ? "Все цифры различны." 
                      : "Есть повторяющиеся цифры.");
}