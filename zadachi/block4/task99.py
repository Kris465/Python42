a, b, c = map(int, input("Введите 3 числа через пробел: ").split())
print(sum(sorted([a, b, c])[1:]))
