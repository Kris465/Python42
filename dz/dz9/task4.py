number = input("Введите любое целое число: ")
result = ''.join([digit for digit in number if digit not in ['3', '6']])
print("Число после удаления цифр 3 и 6:", result)
