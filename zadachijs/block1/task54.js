const prompt = require('prompt-sync')();
let a1 = prompt("Введите первую сторону чемодана");
let a2 = prompt("Введите вторую сторону чемодана");
let a3 = prompt("Введите третью сторону чемодана");

let b1 = prompt("Введите первую сторону коробки");
let b2 = prompt("Введите вторую сторону коробки");
let b3 = prompt("Введите третью сторону коробки");


v_a = a1 * a2 * a3;
v_b = b1 * b2 * b3;

if (v_a > v_b) {
    console.log("Может")
} else {
    console.log("Не может")
};