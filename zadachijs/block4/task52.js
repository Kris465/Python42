const prompt = require('prompt-sync')();

let r = Number(prompt('Введите размер радиуса: '))
let a = Number(prompt('Введите размер стороны a: '))
let b = Number(prompt('Введите размер стороны b: '))

if ((a > (r + 1)) && (a > (r + 1))){
    console.log('Вася сможет это сделать')
} else {
    console.log('Вася не сможет это сделать')
}