const prompt = require('prompt-sync')();
let p = prompt("Введите четырёхзначное число:")
console.log(Math.floor(p / 1000) + Math.floor(p / 100) % 10 + Math.floor(p / 10) % 10 + p % 10) 
