# Дано двузначное число. Определить:
# а) входят ли в него цифры 4 или 7;
# б) входят ли в него цифры 3, 6 или 9.

x = int(input("Введите двузначное число: "))

if '4' in str(x):
    print(f"В вашем числе {x}, содержится число 3)")
elif '7' in str(x):
    print(f"В вашем числе {x}, содержится число 7)")
elif '3' in str(x):
    print(f"В вашем числе {x}, содержится число 3)")
elif '6' in str(x):
    print(f"В вашем числе {x}, содержится число 6)")
elif '9' in str(x):
    print(f"В вашем числе {x}, содержится число 9)")
else:
    print(f"В вашем числе {x} другие числа")
