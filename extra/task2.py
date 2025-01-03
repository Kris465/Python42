'''
1. Четырехзначное число (проверка)
2. Быки - количество угаданных цифр числа
3. Коровы - количество угаданных цифр числа, которые на своих местах

4. При каждом рекурсивном вызове запрашивать число и считать быков и коров.
5. Каждый рекурсивный вызов функции накапливать в переменную.
6. В конце показать пользователю сколько раз функция вызывалась.

'''
from random import randint

key_number = str(randint(1000, 9999))
print(key_number)
count = 0


def guess_number():
    global count
    guess = input("Введите четырехзначное число: ")

    if len(guess) != 4 or not guess.isdigit():
        print("Пожалуйста, введите корректное четырехзначное число.")
        return guess_number()

    count += 1

    bulls = sum(1 for i in guess if i in key_number)
    cows = sum(1 for i in range(4) if guess[i] == key_number[i])

    if bulls == 4:
        print(f"Вы угадали число {key_number} за {count} попыток.")
    else:
        print(f"{bulls} быков, {cows} коров.")
        return guess_number()


guess_number()
