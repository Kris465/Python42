console.log("Даны вещественные положительные числа a, b, c, d. Выяснить, можно ли прямоугольник со сторонами a, b уместить внутри прямоугольника со сторонами c, d так, чтобы каждая из сторон одного прямоугольника была параллельна или перпендикулярна каждой стороне второго прямоугольника. ")

const prompt = require('prompt-sync')();
let a = parseFloat(prompt('Введите A: '));
let b = parseFloat(prompt('Введите B: '));
let c = parseFloat(prompt('Введите C: '));
let d = parseFloat(prompt('Введите C: '));

if (a != b) {
    const res1 = 1

} else {
    const res1 = 0
}

if (a < c && b < d){
    const res2 = 1

} else {
    const res2 = 0
}

function calculatePerimeter(res1, res2,) {
    const perimeter = res1 + res2;
    return { perimeter };
}

if (perimeter = 2){
    console.log("Всё пролезет")
}