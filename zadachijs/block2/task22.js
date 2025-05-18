// Дано натуральное число n (n > 99). Найти: 
// а) число десятков в нем; 
// б) число сотен в нем. 

function countUnitsAndTens(n) {
    if (n <= 99|| !Number.isInteger(n)) {
        throw new Error("n должно быть натуральным числом и больше 99");
    }

    const tens = Math.floor(n / 10) % 10;
    const hund = Math.floor(n / 100);

    return {
        tens: tens,
        hund: hund
    };
}

const number = 345;
const result = countUnitsAndTens(number);

console.log(`Количество десятков в числе ${number}: ${result.tens}`);
console.log(`Количество сотен в числе ${number}: ${result.hund}`);
