function countUnitsAndTens(n) {
    if (n <= 9 || !Number.isInteger(n)) {
        throw new Error("n должно быть натуральным числом и больше 9.");
    }
    
    const units = n % 10;

    const tens = Math.floor(n / 10) % 10;

    return {
        units: units,
        tens: tens,
    };
}

const number = 345;
const result = countUnitsAndTens(number);

console.log(`Количество единиц в числе ${number}: ${result.units}`);
console.log(`Количество десятков в числе ${number}: ${result.tens}`);
