// Дан массив. Все его элементы: 
// а) увеличить в 2 раза; 
// б) уменьшить на число А; 

const prompt = require('prompt-sync')();
let nums = [169, 13, 52, 43];
let A = 14

// a)

let doubled = nums.map(nums => nums * 2);
console.log(doubled);

// b)

let minus = nums.map(nums => nums - A);
console.log(minus)
