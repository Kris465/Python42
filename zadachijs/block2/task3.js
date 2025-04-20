const prompt = require("prompt-sync")();
const kg = Number(prompt("кг: "));

function calculate(kg) {
    let kg2 = kg / 1000;
    return kg2;
}

function end(kg2) {
    let tonn;
    const lastDigit = Math.floor(kg2) % 10;
    const lastTwoDigits = Math.floor(kg2) % 100;
    
    if (lastTwoDigits >= 11 && lastTwoDigits <= 14) {
        tonn = "тонн";
    } else {
        switch(lastDigit) {
            case 1:
                tonn = "тонна";
                break;
            case 2:
            case 3:
            case 4:
                tonn = "тонны";
                break;
            default:
                tonn = "тонн";
        }
    }
    
    return tonn;
}

const kg2 = calculate(kg);
const tonn = end(kg2);

console.log(`как бы ${kg} кг это ${kg2} ${tonn}`)
