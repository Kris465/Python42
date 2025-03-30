const prompt = require('prompt-sync')();

function hasExactlyThreeSameDigits(n) {
    const s = n.toString().padStart(4, '0');
    const count = {};
    
    for (const digit of s) {
        count[digit] = (count[digit] || 0) + 1;
    }
    
    const counts = Object.values(count);
    return counts.includes(3) && !counts.includes(4);
}

const input = prompt("Введите четырёхзначное число: ");
const number = parseInt(input, 10);

if (isNaN(number)) {
    console.log("Ошибка: введите число!");
} else {
    const result = hasExactlyThreeSameDigits(number);
    console.log(result ? "Cодержит ровно три одинаковые цифры." 
                      : "Не содержит ровно три одинаковые цифры.");
}