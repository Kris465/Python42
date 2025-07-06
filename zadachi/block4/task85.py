x = float(input("Введите x: "))

if x == -1:
    y = 1
elif x < -1:
    y = -1
else:
    y = x
    
print("y = ", y)