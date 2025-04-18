//Дано вещественное число a. Пользуясь только операцией умножения, получить 
//а) 3 a и 10 a за четыре операции; 
//б) 4 a и 20 a за пять операций; 
//в) 5 a и 13 a за пять операций; 
//г) 5 a и 19 a за пять операций; 
//д) 2 a , 5 a и 17 a за шесть операций; 
//е) 4 a , 12 a и 28 a за шесть операций.

let a = 3;

//a)
let result_a = a * 3 * 1;
let result_a2 = result_a * 2;
let result_a3 = result_a2 * 2;
console.log(`3a and 10a: ${result_a}`)


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
