document.getElementById('button').addEventListener('click', function() {
    let usd = document.getElementById('USDInput').value;
    let currency = document.getElementById('select').value;
    let mes = document.getElementById('message');

    if (usd) {
        if (currency == 'EUR') {
            mes.textContent = `В ${usd} USD столько EUR: ${usd * 0.9523}`
        }
        if (currency == 'UAN') {
            mes.textContent = `В ${usd} USD столько UAN: ${usd * 7.24}`
        }
        if (currency == 'AZN') {
            mes.textContent = `В ${usd} USD столько EUR: ${usd * 1.70}`
        }
    } else {
        alert('Пожалуйста выберете из выпадающего списка валюту и укажите кол-во USD!!!')
    }
})