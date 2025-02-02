document.getElementById('submitButton').addEventListener('click', function() {
    const inputnumber = parseInt(document.getElementById('numberinput').value);
    let result = '';

    if (!isNaN(inputnumber) && inputnumber > 1 && inputnumber % 2 == 0) {
        for (let i = 2; i <= inputnumber; i++) {
            if (i % 2 == 0) {
                alert(i)
            }
        }
    } else {
        alert(inputnumber -1 )
    }


    document.getElementById('result').textContent = result.trim();
});