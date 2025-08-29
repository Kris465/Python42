k = int(input("введите число:"))
a = 1
f = []
while a < 110:
    b = a // 1
    c = a % 1
    f.append(a)
    f.append(b)
    a += 1
    if 1 <= k <= 222:
        print(f)
        print(f[k])
    else:
        print("операция не сработана")
