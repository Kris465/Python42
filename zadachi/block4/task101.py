num1 = int(input("Введите 1-ое трехзначное число: "))
num2 = int(input("Введите 2-ое трехзначное число: "))

if 99 < num1 and num2 < 1000:
    digits = [int(i) for i in str(num1)]
    mid_num1 = sum(digits) / len(digits)
    print(f"Среднее значение первого числа - {mid_num1}")

    digits2 = [int(i) for i in str(num2)]
    mid_num2 = sum(digits2) / len(digits2)
    print(f"Среднее значение вторго числа - {mid_num2}")
else:
    print("Числа не трехзначные")
