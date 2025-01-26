document.getElementById("yearButton").addEventListener("click", function() {
    const year = Number(document.getElementById("yearInput").value);
    const yearResult = document.getElementById("yearResult");

    if ((year % 400 === 0) || (year % 4 === 0 && year % 100 !== 0)) {
        yearResult.textContent = "Год високосный.";
    } else {
        yearResult.textContent = "Год не високосный.";
    }
});