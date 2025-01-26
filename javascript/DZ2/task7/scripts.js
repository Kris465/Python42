function calculateDiscount(){
    const amount = parseFloat(document.getElementById('amount').value);
    let discount = 0;
     
     if (amount >= 200 && amount < 300){
        discount = 0.03; // 3%
     } else if (amount >= 300 && amount < 500){
        discount = 0.05; // 5%
     } else if (amount >=500){
        discount = 0.07; // 7%
     }
     
     const total = amount - (amount * discount);
     document.getElementById('result').innerText = 'Сумма к оплате: ${total.toFixed(2)} руб.';
} 