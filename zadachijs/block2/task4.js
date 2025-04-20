const prompt = require('prompt-sync')();

let metr = prompt('Введите расстояние в метрах: ')
let km = Math.floor(metr * 0.001)
console.log(`Количество целых километров: ${km}`)