// С начала суток прошло n секунд. Определить: 
// а) сколько полных часов прошло с начала суток; 
// б) сколько полных минут прошло с начала очередного часа; 
// в) сколько полных секунд прошло с начала очередной минуты. 


//a)

const secondsInput = prompt("ВВедите секунды: ");
const seconds = parseInt(secondsInput);

if (isNaN(seconds) || seconds < 0) {
    console.log("Ошибочка)");
} else {
    const fullHours = Math.floor(seconds / 3600);
    console.log(`Вот сколько полных часов: ${fullHours}`);
}

// б)

const minInput = prompt("ВВедите минуты: ");
const mim = parseInt(minInput);

if (isNaN(min) || min < 0) {
    console.log("Ошибочка)");
} else {
    const fullMin = Math.floor(60 / min);
    console.log(`Вот сколько полных минут: ${fullMin}`);
}

// в)

const secInput = prompt("ВВедите секунды: ");
const sec = parseInt(secInput);

if (isNaN(sec) || sec < 0) {
    console.log("Ошибочка)");
} else {
    const fullSec = Math.floor(60 / sec);
    console.log(`Вот сколько полных секунд: ${fullSec}`);
}