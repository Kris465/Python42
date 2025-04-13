const prompt = require('prompt-sync')();

let num = Math.radians(Number(prompt('Введите размер угла в градусах:')));
let sinus = Math.sin(num);
let osn_mal = Number(prompt('Введите размер малого в градусах:'));
let osn_big = Number(prompt('Введите размер большего в градусах:'));

console.log(`Площадь треугольника равна: ${(osn_mal * osn_big) / sinus}`)
