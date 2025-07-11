x = float(input("Введите x: "))
k = float(input("Введите k: "))
if x < k:
    print(f"{abs(x)}")
elif x >= k:
    print(k * x)
else:
    print("не понял")
