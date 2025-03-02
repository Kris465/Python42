// a
console.log("5 10 7 см");

// b
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question('Введите число: ', (t) => {
    readline.question('Введите ещё одно число: ', (v) => {
        console.log(`100 ${t} 1949 ${v}`);
        readline.close();
    });
});

// c
const readline2 = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

readline2.question('Введите число: ', (x) => {
    readline2.question('Введите ещё одно число: ', (y) => {
        console.log(`${x} 25 ${x} ${y}`);
        readline2.close();
    });
});

