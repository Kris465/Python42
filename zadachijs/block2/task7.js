// С начала суток прошло n секунд. Определить: 
// а) сколько полных часов прошло с начала суток; 
// б) сколько полных минут прошло с начала очередного часа; 
// в) сколько полных секунд прошло с начала очередной минуты. 


//a)

const seconds = 3600

if (isNaN(seconds) || seconds < 0) {
    console.log("Ошибочка)");
} else {
    const fullHours = Math.floor(seconds / 3600);
    console.log(`Вот сколько полных часов: ${fullHours}`);
}

// const sec = second % 3600;
// const min = 20

// if (isNaN(min) || min < 0) {
//     console.log("Ошибочка)");
// } else {
//     const fullMin = Math.floor((sec % 3600) / 60);
//     console.log(`Вот сколько полных минут: ${fullMin}`);
// }

// в общем надо подумать:)