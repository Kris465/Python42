def find_pair_number(k):
    if k < 1 or k > 180:
        return " K вне диапазона"
    index = k - 1
    pair_number = index // 2 + 1
    return pair_number


k = int(input("введите число K: "))
reault = find_pair_number(k)
print(f"номер пары цифр для K = {k}: {reault}")
