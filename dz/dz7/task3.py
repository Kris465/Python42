num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

user_list = [i for i in range(num1, num2 + 1)]
for i in user_list:
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
