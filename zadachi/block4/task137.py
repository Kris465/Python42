
k = int(input("введите число: "))
if k <= 1:
    print(k)
elif k <= 180:
    n = k - 1
    num = 10 + (n - 1) // 2
    print(num // 10 if n % 2 == 1 else num % 10)
else:
    print("не в ходит диапазон чисел")

