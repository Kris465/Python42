my_list = [int(i) for i in input("Введите число").split(",")]
summa = 0
proisvedenie = 1
for i in my_list:
    summa += i
    proisvedenie *= i
print(summa, proisvedenie)
