
k = int(input("введите число: "))
i = 10
spisok = []
while i < 100:
    a = i // 10
    b = i % 10
    spisok.append(a)
    spisok.append(b)
    i += 1
print(spisok)
print(spisok[k])
