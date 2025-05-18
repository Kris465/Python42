function findXFromN(n) {
    if (n < 10 || n > 999) {
        return "Число n должно быть в диапазоне от 10 до 999";
    }

    for (let a = 1; a < 10; a++) {
        for (let b = 0; b < 10; b++) {
            let c = n - 10 * a - b;
            if (c >= 0 && c <= 9) {
                let x = 100 * a + 10 * b + c;
                if (x >= 100 && x < 1000) {
                    return { x: x, n: n };
                }
            }
        }
    }

    return "Не удалось найти подходящее число x";
}

const n = parseInt(prompt("Введите значение n (10 ≤ n ≤ 999): "));
const result = findXFromN(n);
console.log("Результат:", result);