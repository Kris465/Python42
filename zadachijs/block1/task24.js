//a
// const prompt = require('prompt-sync')();
// const a = prompt('Введите число "a": ');

// let x = Math.sqrt(2 * a + Math.sin(Math.abs(3 * a)) / 3.56)
// console.log(`Вот значение x =  ${x}`);

//b
const prompt = require('prompt-sync')();
const x = prompt('Введите число "x": ');

let y = Math.sin(3.2 + Math.sqrt(1 + x) / Math.abs(5 * x))
console.log(`Вот значение y =  ${y}`);