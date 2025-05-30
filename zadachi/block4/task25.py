number = int(input("Введите число: "))

if 10 <= number <= 99:
    des = number // 10
    ed = number % 10
    new = des + ed
    print("Число двузначное")
else:
    print("Не двузначное число!")


if 10 <= new <= 99:
    print(f"Сумма: {des} и {ed} является двузначным! ({new})")
else:
    print(f"Сумма: {des} и {ed} не является двузначным! ({new})")


if new > number:
    print(f"Сумма чисел {des} и {ed} больше ", number)
else:
    print(f"Сумма чисел {des} и {ed} меньше ", number)
