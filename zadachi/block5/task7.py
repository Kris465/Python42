a = 20.1
b = 2

while True:
    c = round(b * a, 2)
    print(f"{b} единиц товара будет: {c} Евробаксов")
    if b == 20:
        break
    b = b + 1
