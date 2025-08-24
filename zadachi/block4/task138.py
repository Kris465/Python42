n = int(input("введите число что хотите найти в текущем списке: "))
if n <= 9:
    print(n)
elif n <= 31:
    k = n - 9
    num = 10 + (k - 1) // 2
    print(num // 10 if k % 2 == 1 else num % 10)
else:
    print("не в ходит диапазон чисел")
