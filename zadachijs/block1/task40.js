
function calculateF(x, a, b) {
    return a * Math.pow(x, 2) + b * x + a * b;
}

function calculateG(x, a, b) {
    return 2 * Math.sin(a * x + b);
}


let a = 3;
let b = 4;
let x = 2; 

console.log("f(x) = " + calculateF(x, a, b)); 
console.log("g(x) = " + calculateG(x, a, b)); 