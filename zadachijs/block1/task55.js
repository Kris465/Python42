const prompt = require('prompt-sync')();
let x1 = Number(prompt('Введите первой машины'));
let y1 = Number(prompt('Введите скорость второй машины'));
let y2 = Number(prompt('Введите расстояние'));
console.log(`автомобили встретятся через: ${y2 / (y1 + x1)} ч`);
