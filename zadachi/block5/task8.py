g = 453
f = 1
while True:
    scolco = round(f * g, 2)
    print(f"{f} фунт: {scolco} грамм")
    if f == 10:
        break
f = f + 1
