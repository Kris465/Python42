document.getElementById("yearButton").addEventListener("click", function() {
    const year = document.getElementById("dateInput").value;
    const message = document.getElementById("result")

    good = new Date(year);
    good.setDate(good.getDate() + 1);
    message.textContent = good;
});