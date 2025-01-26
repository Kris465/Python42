
n = int(input("Введите n"))
if 1 <= n <= 999:
    y = str(n)
    b = n - int(y[-1])
    m = b / 10
    x = str(y[-1]) + str(m)
    print(x)
