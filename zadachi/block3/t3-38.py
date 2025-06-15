k = int(input("\nВведите целое число от 1 до 180: "))

# а)
id_para = int(round(k/2 + 0.1, 0))
print(f"\nЗадание А) Номер пары цифр, в которую входит k-я цифра: {id_para}")

# б)
chislo = 10 + (id_para - 1)
print("Задание Б) Двузначное число, образованное парой цифр,",
      f"в которую входит k-я цифра: {chislo}")

# в)
if k % 2 == 0:
    cifra_k = chislo % 10
    print(f"Задание В) k-я цифра: {cifra_k}")
else:
    cifra_k = chislo // 10
    print(f"Задание В) k-я цифра: {cifra_k}")