// Дано вещественное число а. Пользуясь только операцией умножения, полу
// чить: 
// а) 4 a за две операции; 
// б) 6 a за три операции; 
// в) 7 a за четыре операции; 
// г) 8 a за три операции; 
// д) 9 a за четыре операции; 
// е) 10 a за четыре операции; 


let a = 2;

// а)
let result_a = a * 2 * 2;
console.log(`4a: ${result_a}`);

// б)
let result_b = a * 2 * 3;
console.log(`6a: ${result_b}`);

// в)
let temp1 = a * 2; // (2a)
let temp2 = temp1 * 3; // (6a)
let result_c = temp1 + temp2;
result_c = (temp1 * 3) + (temp1);
console.log(`7a: ${result_c}`);

// г)
let result_d = a * 4; // (4a)
console.log(`8a: ${result_d}`);

// д)
let temp3 = a * 3; // (3a)
let result_e = temp3 * 3;
result_e = (temp3 + temp3) + a;
console.log(`9a: ${result_e}`);

// е)
let temp4 = a * 5; // (5a)
let result_f = temp4 * 2;
result_f = (temp4 + temp4) - a;
console.log(`10a: ${result_f}`);
