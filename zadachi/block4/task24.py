n = int(input("Выведите двузначное число: "))

a = n // 10
b = n % 10

kv_chisla = n ** 2
sum = a ** 3 + b ** 3
sum_in_4_stepen = 4 * (a ** 3 + b ** 3)

if sum_in_4_stepen > kv_chisla:
    print(f"{sum_in_4_stepen}")
else:
    print("Значит не то")
