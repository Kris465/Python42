num = int(input("Введите трехзначное число: "))
if 100 <= num < 999:
    str_name = str(num)
    swapped_name = int(str_name[2] + str_name[1] + str_name[0])
else:
    print("Не то)")
print("Твое число теперь такое >:) --->", swapped_name)
