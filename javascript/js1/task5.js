const prompt = require('prompt-sync')();

// Составьте выражение, которое истинно при четных значениях переменной «х» из диапазона 0–10
// и ложно для других значений (например, х=0 — истина, х=3 —
// ложь, х=8 — истина, х=–1 — ложь, х=10 — истина,
// х=12 — ложь).

let x = prompt("ввидите число:");

if (x>=0 && x<=10 && (x % 2 == 0)) {
    console.log('истина');
} else {
    console.log('ложь');
}