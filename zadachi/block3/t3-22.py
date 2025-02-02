# Вычислить значение логического выражения при всех возможных значениях
# логических величин X, Y и Z:
# а) не (X или не Y и Z);
# б) Y или (X и не Y или Z);
# в) не (не X и Y или Z).

    # 1
# x = True
# y = True
# z = True

    # 2
# x = False
# y = True
# z = True

    # 3 
# x = True
# y = False
# z = True

    # 4 
# x = True
# y = True
# z = False

    # 5 
# x = False
# y = False
# z = True

    # 6 
# x = False
# y = True
# z = False

    # 7 
# x = True
# y = False
# z = False

    # 8 
x = False
y = False
z = False


print(not (x or not y and z))
print(y or (x and not y or z))
print(not (not x and y or z))
