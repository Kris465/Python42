const prompt = require("prompt-sync")();

const prise_apple = prompt("Введите стоимость яблок за 1 кг: ")
const prise_candy = prompt("Введите стоимость конфеток за 1 кг: ")
const prise_coockie = prompt("Введите стоимость печенек за 1 кг: ")

const weight_apple = prompt("Введите кол-во взятых кг яблок: ")
const weight_candy = prompt("Введите кол-во взятых кг конфеток: ")
const weight_coockie = prompt("Введите кол-во взятых кг печенек: ")

all_sum = (prise_apple * weight_apple) + (prise_candy * weight_candy) + (prise_coockie * weight_coockie)

console.log(`Сумма покупки равна: ${all_sum}`)