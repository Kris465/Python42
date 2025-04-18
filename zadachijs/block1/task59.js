const prompt = require("prompt-sync")();
let t1 = Number(prompt("значения a: "));
let t2 = Number(prompt("значения b: "));
let t11 = t1
console.log(`a = было ${t1}`)
console.log(`b = было ${t2}`)
swap(t1,t2,t11);
function swap(t1, t2, t11) {
    t1 = t2
    t2 = t11

    console.log(`a = стало ${t1}`)
    console.log(`b = стало ${t2}`)

    // return t1, t2
}

