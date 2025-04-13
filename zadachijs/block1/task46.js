// Даны длины сторон прямоугольного параллелепипеда. Найти его объем и 
// площадь боковой поверхности. 
const prompt = require('prompt-sync')();
let x = Number(prompt('Введите длину: '));
let y = Number(prompt('Введите ширину: '));
let z = Number(prompt('Введите ребро: '));
console.log(`Объём равен = ${x * y * z}`)
console.log(`Площадь боковой стороны равна = ${x * y}`)
