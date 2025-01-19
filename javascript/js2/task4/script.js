document.getElementById('button').addEventListener('click', function(){
    
    const num = document.getElementById('num').value;
    const numTwo = document.getElementById('numTwo').value;

    const message = document.getElementById('message');

    if (Number(num) == Number(numTwo)){
        message.textContent = `Числа равны`
    }else if (Number(num) >= Number(numTwo)){
        message.textContent = `Число ${num} больше числа ${numTwo}`
    }else{
        message.textContent = `Число ${num} меньше числа ${numTwo}`

    }

})