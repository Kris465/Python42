let h = parseInt(prompt("введите введите высоту: "));
let r = 6350;
let d = round((((r + h) ** 2) - (r ** 2)) ** 0.5 , 2);
console.log(`Растояние до линии горизонта = ${d} км`);