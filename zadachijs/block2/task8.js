// Дано целое число k (1 ≤ k ≤ 365). Присвоить целочисленной величине n значе
// ние 1, 2, ..., 6 или 0 в зависимости от того, на какой день недели (понедельник, 
// Глава 2 
// 12 
// вторник,  ..., субботу или воскресенье) приходится k-й день года, в котором 
// 1 января: 



function getDayOfWeek(k) {
    
    if (k < 1 || k > 365) {
        throw new Error("k должно быть в диапазоне от 1 до 365");
    }

    
    const dayOfWeek = (k % 7);
    
    return dayOfWeek === 0 ? 0 : dayOfWeek;
}

const k = 10; 
const n = getDayOfWeek(k);
console.log(`День недели для ${k}-го дня года: ${n}`);

// const prompt = require('prompt-sync')();
// let k = prompt('Введите число от 1 до 365');
// if (Math.log(k / 7)){
// console.log("n = 0")
// }else if(Math.log(k / 6)){
//     console.log("n = 1")
// }else if(Math.log(k / 5)){
//     console.log("n = 2")
// }else if(Math.log(k / 4)){
//     console.log("n = 3")
// }else if(Math.log(k / 3)){
//     console.log("n = 4")
// }else if(Math.log(k / 2)){
//     console.log("n = 5")
// }else{
//     console.log("n = 6")
// }
