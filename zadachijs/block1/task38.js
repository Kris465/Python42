function calculatePerimeter(a, b, h) {
    const halfBaseDifference = (a - b) / 2;
    const sideLength = Math.sqrt(h * h + halfBaseDifference * halfBaseDifference);
    
    const perimeter = a + b + 2 * sideLength;
    return perimeter;
}


const prompt = require('prompt-sync')();
let a = prompt('введите А периметра равнобедренной трапеции: ');
let b = prompt('введите B периметра равнобедренной трапеции: ');
let h = prompt('введите H периметра равнобедренной трапеции: '); 

const perimeter = calculatePerimeter(a, b, h);
console.log(`Периметр равнобедренной трапеции: ${perimeter}`);
