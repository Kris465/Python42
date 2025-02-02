# Вычислить значение логического выражения при всех возможных значениях
# логических величин X, Y и Z:
# а) не (Y или не X и Z) или Z;
# б) X и не (не Y или Z) или Y;
# в) не (X или Y и Z) или не X.

# version 1

x = False
y = False
z = False

print( not (y or not x and z) or z)
print(x and not (not y or z) or y)
print(not (x or y and z) or not x)

# version 2

x = False
y = False
z = True

print( not (y or not x and z) or z)
print(x and not (not y or z) or y)
print(not (x or y and z) or not x)

# version 3

x = False
y = True
z = False

print( not (y or not x and z) or z)
print(x and not (not y or z) or y)
print(not (x or y and z) or not x)

# version 4

x = True
y = False
z = False

print( not (y or not x and z) or z)
print(x and not (not y or z) or y)
print(not (x or y and z) or not x)

# version 5

x = False
y = True
z = True

print( not (y or not x and z) or z)
print(x and not (not y or z) or y)
print(not (x or y and z) or not x)

# version 6

x = True
y = False
z = True

print( not (y or not x and z) or z)
print(x and not (not y or z) or y)
print(not (x or y and z) or not x)

# version 7

x = True
y = True
z = False

print( not (y or not x and z) or z)
print(x and not (not y or z) or y)
print(not (x or y and z) or not x)

# version 8

x = True
y = True
z = True

print( not (y or not x and z) or z)
print(x and not (not y or z) or y)
print(not (x or y and z) or not x)
