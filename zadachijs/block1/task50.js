const prompt = require('prompt-sync')();
let x1 = Number(prompt('Введите координат x'));
let y1 = Number(prompt('Введите координат y'));
let x2 = Number(prompt('Введите координат x'));
let y2 = Number(prompt('Введите координат y'));
let x3 = Number(prompt('Введите координат x'));
let y3 = Number(prompt('Введите координат y'));
let a = Math.sqrt((x2-x1)+(y2-y1));
let b = Math.sqrt((x3-x2)+(y3-y2));
let c = Math.sqrt((x1-x3)+(y1-y3));
let p = (a + b + c)/2;
console.log(`S = ${Math.sqrt(p*(p - a)*(p - b)*(p - c))}`);
console.log(`P = ${a + b + c}`);   
