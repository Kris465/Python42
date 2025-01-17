document.getElementById('Button').addEventListener('click', function() {
    const summa = parseFloat(document.getElementById('summa').value);
    const chok = parseFloat(document.getElementById('chok').value);

    if (!isNaN(summa) && summa > 0 && !isNaN(chok) && chok > 0) {
        const colvo = Math.floor(summa / chok);
        const ostatok = summa % chok;
        document.getElementById('result').innerText = `Сколько вы купили шоколадок: ${colvo.toFixed(2)}, ваша сдача ${ostatok.toFixed(2)}`;

    } else{
        document.getElementById('result').innerText = 'Пожалуйста, введите нормально...';
    }
});