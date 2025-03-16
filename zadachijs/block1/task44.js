function calculatePerimeter(a, b) {
    const perimeter = (a * 2) + (b * 2);
    const a1 = a * a;
    const b2 = b * b;
    const dlina = Math.sqrt(a1 + b2);
    return { perimeter, dlina };
}

const prompt = require('prompt-sync')();
let a = parseFloat(prompt('Введите A периметра прямоугольника: '));
let b = parseFloat(prompt('Введите B периметра прямоугольника: '));

const { perimeter, dlina } = calculatePerimeter(a, b);
console.log(`Периметр: ${perimeter}, длина: ${dlina}`);
