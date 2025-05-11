function swapDigits(number) {
    if (number < 10 || number > 99) {
      return "Ошибка: число должно быть двузначным (10-99)";
    }
  
    const tens = Math.floor(number / 10);  
    const units = number % 10;            
    const swappedNumber = units * 10 + tens;
    return swappedNumber;
  }
  
  const num = 57;
  const result = swapDigits(num);
  
  console.log(`Исходное число: ${num}`);
  console.log(`Число после перестановки цифр: ${result}`);