# Вычислить значение логического выражения при всех возможных значениях 
# логических величин X и Y:
# а) не (X и не Y) или X;
# б) Y и не X или не Y;
# в) не Y и не X или Y.

# 1 versin

X = True
Y = True

print(not (X and not Y) or X)
print(Y and not X or not Y)
print(not Y and not X or Y)

# 2 version

X = True
Y = False

print(not (X and not Y) or X)
print(Y and not X or not Y)
print(not Y and not X or Y)

# 3 version

X = False
Y = True

print(not (X and not Y) or X)
print(Y and not X or not Y)
print(not Y and not X or Y)

# 4 version

X = False
Y = False

print(not (X and not Y) or X)
print(Y and not X or not Y)
print(not Y and not X or Y)