def hz(num, index):
    if num < 100:
        if index == 0:
            return num // 10
        else:
            return num % 10
    else:
        if index == 0:
            return num // 100
        elif index == 1:
            return (num // 10) % 10
        else:
            return num % 10


def findk(k):
    if k <= 100 and k <= 252:
        num = ((k - 1) // 2 + 50)
        index = ((k - 1) % 2)
        return hz(num, index)

    if k > 100:
        pos = k - 100
        num = (pos - 1) // 3 + 100
        index = (pos - 1) % 3
        return hz(num, index)


k = int(input("Введите k: "))
print(findk(k))
