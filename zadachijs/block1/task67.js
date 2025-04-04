


const prompt = require('prompt-sync')();
let k = prompt("Введите k день  ");
const date = new Date(k);
const options = { weekday: 'long' };
const dayOfWeek = date.toLocaleString('en-US', options);
console.log(dayOfWeek);