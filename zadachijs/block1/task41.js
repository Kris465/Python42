//a)


// const prompt = require('prompt-sync')();
// const e = prompt('Введите число "e": ');
// const f = prompt('Введите число "f": ');
// const g = prompt('Введите число "g": ');



// let a = Math.sqrt(Math.pow((Math.abs(e - (3 / f)) , 3) + g))
// console.log(`Вот значение a =  ${a}`);


//b)
// const prompt = require('prompt-sync')();
// const e = Number(prompt('Введите число "e": '));
// const h = Number(prompt('Введите число "h": '));

// let b = Math.sin(e) + Math.pow((Math.cos(h) , 2))
// console.log(`Вот значение b =  ${b}`);

//c)
const prompt = require('prompt-sync')();
const g = prompt('Введите число "g": ');
const e = prompt('Введите число "e": ');
const f = prompt('Введите число "f": ');



let c = (33 * g) / (e * f - 3)
console.log(`Вот значение c =  ${c}`);
