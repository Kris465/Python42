function calculateY(x) {
    let y;

    if (x > 0) {
        y = Math.pow(Math.sin(x), 2);
    } else {
        y = 1 + 2 * Math.pow(Math.sin(x), 2);
    }

    return y;
}

const x = 1; 
const result = calculateY(x);
console.log(`При x = ${x}, y = ${result}`);