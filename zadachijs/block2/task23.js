const prompt = require('prompt-sync')();
let p = prompt("Введите четырёхзначное число, которое больше 999: ")
console.log(`Количество сотен: ${Math.floor(p / 100) % 10}`)
console.log(`Количество тысяч: ${Math.floor(p / 1000)}`)