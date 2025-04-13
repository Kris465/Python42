//Даны основания и высота равнобедренной трапеции. Найти периметр трапеции. 

const prompt = require('prompt-sync')();
let x = Number(prompt('Введите первое основание трапеции: '));
let y = Number(prompt('Введите второе основание трапеции: '));
let z = Number(prompt('Введите высоту трапеции: '));
const a = (x - y) / 2;
const b = Math.sqrt ((Math.pow(z, 2)) + (Math.pow(a, 2)));

console.log(`Периметр трапеции равен = ${x + y + (2 * b)}`);
 