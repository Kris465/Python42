num = int(input("Введите число: "))
if num[0] * num[0] == num[0:1] * num[0:1] * num[0:1] + num[1:2] * num[1:2] * num[1:2] + num[2:3] * num[2:3] * num[2:3]:
    print("они равны")
else:
    print("не равны")