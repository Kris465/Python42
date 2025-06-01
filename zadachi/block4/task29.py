number = int(input("Введите трехзначное число: "))

digit1 = number // 100         
digit2 = (number // 10) % 10    
digit3 = number % 10           
square = number ** 2

sum_of_cubes = digit1**3 + digit2**3 + digit3**3

if square == sum_of_cubes:
    print(f"Квадрат числа {number} равен сумме кубов его цифр.")
else:
    print(f"Квадрат числа {number} НЕ равен сумме кубов его цифр.")
    
print("я сделал это задание, лол если фрол не посмотрит это задание, то я очень силбно обижусь на него")
