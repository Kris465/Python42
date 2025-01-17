
const USD_TO_EUR_RATE = 0.976025;

function convertUsdToEur() {
    let usdAmount = document.getElementById("usdAmount").value; 
    usdAmount = parseFloat(usdAmount); 

    if (!isNaN(usdAmount) && usdAmount >= 0) {
        let eurAmount = (usdAmount * USD_TO_EUR_RATE).toFixed(2); 
        alert(usdAmount + " долларов = " + eurAmount + " евро."); 
    } else {
        alert("Пожалуйста, введите корректное значение суммы в долларах.");
    }
}

document.getElementById("convertButton").addEventListener("click", convertUsdToEur);