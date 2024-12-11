n = int(input("Введите сторону: "))

# квадратик
# print(*[''.join([" * " for elem in range(n)]) + "\n" for i in range(n)])

# диагональка

for i in range(n):
    for j in range(n):
        if j <= i:
            print(" * ", end='')
        else:
            print("   ", end='')
    print()

print()

for i in range(n):
    for j in range(n):
        if j <= i:
            print("   ", end='')
        else:
            print(" * ", end='')
    print()

