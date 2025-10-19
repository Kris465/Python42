summa = 1
x = 2
n = False

for i in range(2, 11):
    if n is False:
        summa -= i/(i + 1) * x**(i - 1)
        n = True
    else:
        summa += i/(i + 1) * x**(i - 1)
        n = False

print(summa)
