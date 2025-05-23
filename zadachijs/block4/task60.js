
let a = 1;
let b = 2;
let c = 3;

console.log("Исходные значения:");
console.log(`a = ${a}, b = ${b}, c = ${c}`);

let temp = b; й
b = c;       
a = temp;

console.log("\nПосле схемы а):");
console.log(`a = ${a}, b = ${b}, c = ${c}`);

temp = b;  
b = a;       
c = temp;    

console.log("\nПосле схемы б):");
console.log(`a = ${a}, b = ${b}, c = ${c}`);