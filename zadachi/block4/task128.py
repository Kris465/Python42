num = int(input("Введите кол-во месяцев (от 1 до 1188): "))  # меясцы

if num > 1 and num < 1189:
    year = num // 12  # года
    month = num % 12  # месяцы
    print(f'Вам {year} лет и {month} месяцев')
