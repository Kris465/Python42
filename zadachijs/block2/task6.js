// С начала суток прошло n секунд. Определить: 
// а) сколько полных часов прошло с начала суток; 
// б) сколько полных минут прошло с начала очередного часа; 
// в) сколько полных секунд прошло с начала очередной минуты.

const prompt = require('prompt-sync')();
const n = Number(prompt('Введите количество секунд "n": '));

const hour = n / 3600;
const minutes = (n / 3600) - (n / 60);
const seconds = n - (n / 60);


console.log(hour);
console.log(minutes);
console.log(seconds);
