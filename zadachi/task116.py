def calculate_difference(a2, a1, b):
    
    a = a2 * 10 + a1
    
    difference = a - b

    tens = difference // 10  
    units = difference % 10  
    
    return tens, units

a2 = int(input("Введите цифру десятков (a2): "))
a1 = int(input("Введите цифру единиц (a1): "))
b = int(input("Введите однозначное число (b): "))

tens, units = calculate_difference(a2, a1, b)
print(f"Цифры числа разности: десятки = {tens}, единицы = {units}")
