n = int(input("Введите кол-во кепеек (от 1 до 9999): "))  # копейки

if n > 1 and n < 9999:
    rub = n // 100  # рубли
    kop = n % 100  # копейки
    if kop == 0:
        if rub == 1:
            print('У вас ровно 1 рубль!')
        elif rub > 1 and rub < 5:
            print(f'У вас ровно {rub} рубля!')
        else:
            print(f'У вас ровно {rub} рублей!')
    else:
        if rub == 1:
            if kop == 1:
                print('У вас ровно 1 рубль и 1 копейка!')
            elif kop > 1 and kop < 5:
                print(f'У вас ровно 1 рубль и {kop} копейки!')
            else:
                print(f'У вас ровно 1 рубль и {kop} копееек')

        elif rub > 1 and rub < 5:
            if kop == 1:
                print('У вас {rub} рубля и 1 копейка!')
            elif kop > 1 and kop < 5:
                print(f'У вас {rub} рубля и {kop} копейки!')
            else:
                print(f'У вас {rub} рубля и {kop} копееек!')

        else:
            if kop == 1:
                print('У вас {rub} рублей и 1 копейка!')
            elif kop > 1 and kop < 5:
                print(f'У вас {rub} рублей и {kop} копейки!')
            else:
                print(f'У вас {rub} рублей и {kop} копееек!')
