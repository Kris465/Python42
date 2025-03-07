const prompt = require('prompt-sync')();
const x = prompt('Введите см сторону квадрата ');
if (x > 0){
    console.log(`Периметр квадрата равен: ${4 * x} см`)
}
else {
    console.log("такого квадрата не существует");
}