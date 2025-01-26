document.getElementById('Button').addEventListener('click', function() {
    const num = document.getElementById('numInput').value;
    const result = document.getElementById('result');
    
    const isPalindrome = num == num.split('').reverse().join('');
    result.textContent = isPalindrome ? 'число является палиндромом' : 'число не является палиндромом';

});