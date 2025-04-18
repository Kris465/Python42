// Известна стоимость монитора, системного блока, клавиатуры и мыши. 
//Сколько будут стоить 3 компьютера из этих элементов? N компьютеров? 
function calculateTotalCost(monitorPrice, systemUnitPrice, keyboardPrice, mousePrice, numberOfComputers) {
    const costPerComputer = monitorPrice + systemUnitPrice + keyboardPrice + mousePrice

    const totalCost = costPerComputer * numberOfComputers;
    
    return totalCost;
}

const monitorPrice = 50; 
const systemUnitPrice = 500; 
const keyboardPrice = 30;
