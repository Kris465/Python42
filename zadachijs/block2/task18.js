// Дан массив. Все его элементы: 
// а) уменьшить в 20 раз; 
// б) уменьшить на послежний элемент;
// в) увеличить число на B

const prompt = require('prompt-sync')();
let nums = [169, 13, 52, 43];
let B = 14

// a)

let doubled = nums.map(nums => nums - 20);
console.log(doubled);

// b)

let minus = nums.map(nums => nums - 43);
console.log(minus)


// v)

let plus = nums.map(nums => nums + B);
console.log(minus)