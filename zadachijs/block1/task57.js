const prompt = require("prompt-sync")();
const t1 = Number(prompt("Введите температуру по Цельсия: "));

const t2 = t1 * 1.8 + 32;
const t3 = t1 + 273.15;
console.log(`Температура по Фаренгейту будет ${t2}`);
console.log(`Температура по Кельвину будет ${t3}`);
