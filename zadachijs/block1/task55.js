const prompt = require('prompt-sync')();
let x = prompt("Введите число: ");
let a = prompt("Введите значение a: ");

if (100 > x > 9){
    res1 = 1;
} else {
    res1 = 0;
    console.log("НЕ Соблюдено");
}

if (3 < x || 3 == x){
    res2 = 1;
} else {
    res2 = 0;
    console.log("НЕ Соблюдено");   
}

if (a < x || a == x){
    res3 = 1;
} else {
    res3 = 0;
    console.log("НЕ Соблюдено");
}

function summa(res1, res2, res3) {
    const ressum = res1 + res2 + res3
    return ressum
}

if (ressum == 3){
    console.log("Все условия соблюдены")
} else {
    console.log("Что-то не так")
}