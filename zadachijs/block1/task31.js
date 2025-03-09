
function calculateMeans(a, b) {

    let arithmeticMean = (a + b) / 2;

    let geometricMean = Math.sqrt(a * b);

    console.log("Среднее арифметическое: " + arithmeticMean);
    console.log("Среднее геометрическое: " + geometricMean);
}
let num1 = 4;
let num2 = 9;
calculateMeans(num1, num2);