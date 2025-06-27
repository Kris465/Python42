from collections import Counter

n = int(input("Введите 4-х значное число!: "))


def yabloko(n):
    s = str(n).zfill(4)
    counts = Counter(str(s)).values()
    return 3 in counts and 1 in counts and sum(v for v in counts if v != 3 and v != 1 == 0)


res = yabloko(n)


# if res == 0:
#     r = "есть три числа которые повторяются"
# elif res == False:
#     r = "нет трёх чисел которые повторяются"

print(res)
