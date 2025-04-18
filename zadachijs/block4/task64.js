const prompt = require('prompt-sync')();
console.log("Введите 6-ти значное число: ")
const number = prompt();

let n1 = parseInt(number[0]) 
let n2 = parseInt(number[1])
let n3 = parseInt(number[2])
let n4 = parseInt(number[3])
let n5 = parseInt(number[4])
let n6 = parseInt(number[5])

if ( n1 + n2 + n3 == n4 + n5 + n6) {
    console.log("Поздравляем! Ваше число счастливое!")
} else {
    console.log("К сожалению ваше число не счастливое. Но ничего в следующий раз повезёт!")
}