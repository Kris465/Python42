const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

/**
 * Определяет k-ю цифру в последовательности 101102...150
 * в зависимости от типа k.
 *
 * @param {number} k - Искомое число.
 * @param {string} type - Тип k ('multipleOf3', 'oneOf1_4_7', 'oneOf2_5_8').
 * @returns {string|number} - Найденная цифра или сообщение об ошибке.
 */
function findKthDigit(k, type) {
    if (k < 1 || k > 150) {
        return "Значение k должно быть в диапазоне от 1 до 150.";
    }

    let blockIndex;
    let targetNumber;
    let digit;

    switch (type) {
        case 'multipleOf3': // k - число, кратное трем
            if (k % 3 !== 0) {
                return "Для этого случая k должно быть кратно 3.";
            }
            // k-я цифра всегда будет последней цифрой числа.
            // Порядковый номер числа (начиная с 1): k / 3
            blockIndex = (k / 3) - 1; // Индекс числа (начиная с 0)
            targetNumber = 101 + blockIndex;
            digit = targetNumber % 10; // Последняя цифра
            break;

        case 'oneOf1_4_7': // k - одно из чисел 1, 4, 7, ...
            if ((k - 1) % 3 !== 0) {
                return "Для этого случая k должно быть вида 3n + 1.";
            }
            // k-я цифра всегда будет первой цифрой числа.
            blockIndex = (k - 1) / 3; // Индекс числа (начиная с 0)
            targetNumber = 101 + blockIndex;
            digit = Math.floor(targetNumber / 100); // Первая цифра
            break;

        case 'oneOf2_5_8': // k - одно из чисел 2, 5, 8, ...
            if ((k - 2) % 3 !== 0) {
                return "Для этого случая k должно быть вида 3n + 2.";
            }
            // k-я цифра всегда будет второй цифрой числа.
            blockIndex = (k - 2) / 3; // Индекс числа (начиная с 0)
            targetNumber = 101 + blockIndex;
            digit = Math.floor((targetNumber % 100) / 10); // Вторая цифра
            break;

        default:
            return "Неизвестный тип k. Используйте 'multipleOf3', 'oneOf1_4_7' или 'oneOf2_5_8'.";
    }

    return digit;
}


rl.question('Введите целое число k (от 1 до 150): ', (kInput) => {
    const k = parseInt(kInput);

    if (isNaN(k)) {
        console.log("Введено некорректное число.");
        rl.close();
        return;
    }

    console.log("\nВыберите тип условия для k:");
    console.log("1. k - число, кратное трем (например: 3, 6, 9, ...)");
    console.log("2. k - одно из чисел 1, 4, 7, ...");
    console.log("3. k - одно из чисел 2, 5, 8, ...");
    rl.question('Введите номер типа (1, 2 или 3): ', (typeInput) => {
        let type;
        switch (typeInput.trim()) {
            case '1':
                type = 'multipleOf3';
                break;
            case '2':
                type = 'oneOf1_4_7';
                break;
            case '3':
                type = 'oneOf2_5_8';
                break;
            default:
                console.log("Неверный выбор типа. Пожалуйста, введите 1, 2 или 3.");
                rl.close();
                return;
        }

        const result = findKthDigit(k, type);
        console.log(`\nРезультат для k = ${k} (${type}): ${result}`);
        rl.close();
    });
});