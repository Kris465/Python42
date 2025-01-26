def find_kth_digit(k):
    sequence = ''.join(str(i) for i in range(101, 151))
    if 1 <= k <= len(sequence):
        return sequence[k - 1]
    else:
        return None


k = int(input("Введите значение k (кратное 3): "))
if k % 3 == 0:
    digit = find_kth_digit(k)
    if digit is not None:
        print(f"Цифра на позиции {k}: {digit}")
    else:
        print("Значение k вне допустимого диапазона.")
else:
    print("k должно быть кратно 3.")
