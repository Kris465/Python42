const prompt = require('prompt-sync')();
let numberWithDigits = prompt("Введите четырёхзначное число:")

function processNumberWithDigits(number) {
    if (number < 1000 || number > 9999) {
        throw new Error("Число должно быть четырехзначным.");
    }
    
    const thousands = Math.floor(number / 1000);
    const hundreds = Math.floor((number % 1000) / 100);
    const tens = Math.floor((number % 100) / 10);
    const units = number % 10;

    const reversed = units * 1000 + tens * 100 + hundreds * 10 + thousands;

    const rearranged1 = hundreds * 1000 + thousands * 100 + units * 10 + tens;

    const rearranged2 = thousands * 1000 + tens * 100 + hundreds * 10 + units;

    const rearranged3 = tens * 1000 + units * 100 + thousands * 10 + hundreds;

    return {
        reversed,
        rearranged1,
        rearranged2,
        rearranged3,
    };
}

const resultWithDigits = processNumberWithDigits(numberWithDigits);

console.log(`Число, прочитанное справа налево (с выделением цифр): ${resultWithDigits.reversed}`);
console.log(`Число с переставленными первой и второй, третьей и четвертой цифрами (с выделением цифр): ${resultWithDigits.rearranged1}`);
console.log(`Число с переставленными второй и третьей цифрами (с выделением цифр): ${resultWithDigits.rearranged2}`);
console.log(`Число с переставленными первыми двумя и последними двумя цифрами (с выделением цифр): ${resultWithDigits.rearranged3}`);