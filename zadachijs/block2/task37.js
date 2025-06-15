const prompt = require('prompt-sync')();
let k = parseInt(prompt("Введите значение для k: "));

function solveKthDigitProblem(k) {
    if (k < 1 || k > 180) {
        return "Ошибка: k должно быть целым числом в диапазоне от 1 до 180.";
    }

    const pairIndex = Math.ceil(k / 2);

    console.log(`а) Номер пары цифр, в которую входит ${k}-я цифра: ${pairIndex}`);

    const twoDigitNumber = 10 + (pairIndex - 1);

    console.log(`б) Двузначное число, образованное парой цифр, в которую входит ${k}-я цифра: ${twoDigitNumber}`);

    let kthDigit;
    if (k % 2 !== 0) {
        kthDigit = Math.floor(twoDigitNumber / 10);
        console.log(`в) ${k}-я цифра (k - нечетное): ${kthDigit}`);
    } else {
        kthDigit = twoDigitNumber % 10;
        console.log(`в) ${k}-я цифра (k - четное): ${kthDigit}`);
    }

    return {
        pairIndex: pairIndex,
        twoDigitNumber: twoDigitNumber,
        kthDigit: kthDigit
    };
};

console.log("\n--- Тест для k = 1 (1-я цифра в 10) ---");
solveKthDigitProblem(1);

console.log("\n--- Тест для k = 2 (2-я цифра в 10) ---");
solveKthDigitProblem(2);

console.log("\n--- Тест для k = 3 (1-я цифра в 11) ---");
solveKthDigitProblem(3);

console.log("\n--- Тест для k = 179 (1-я цифра в 99) ---");
solveKthDigitProblem(179);

console.log("\n--- Тест для k = 180 (2-я цифра в 99) ---");
solveKthDigitProblem(180);

console.log("\n--- Тест для k = 10 (2-я цифра в 14) ---");
solveKthDigitProblem(10);

console.log("\n--- Тест для k = 9 (1-я цифра в 14) ---");
solveKthDigitProblem(9);

console.log("\n--- Тест для k вне диапазона (k = 0) ---");
console.log(solveKthDigitProblem(0));

console.log("\n--- Тест для k вне диапазона (k = 181) ---");
console.log(solveKthDigitProblem(181));