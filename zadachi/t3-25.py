# . Вычислить значение логического выражения при всех возможных значениях
# логических величин А, В и С:
# а) не (А и В) и (не А или не С);
# б) не (А и не В) или (А или не С);
# в) А и не В или не (А или не С).

# 1 version

A = False
B = False
C = False

print(not (A and B) and (not A or not C))
print(not (A and not B) or (A or not C))
print(A and not B or not (A or not C))

# 2 version

A = True
B = True
C = True

print(not (A and B) and (not A or not C))
print(not (A and not B) or (A or not C))
print(A and not B or not (A or not C))

# 3 version

A = True
B = False
C = False

print(not (A and B) and (not A or not C))
print(not (A and not B) or (A or not C))
print(A and not B or not (A or not C))

# 4 version

A = False
B = True
C = True

print(not (A and B) and (not A or not C))
print(not (A and not B) or (A or not C))
print(A and not B or not (A or not C))

# 5 version

A = False
B = True
C = False

print(not (A and B) and (not A or not C))
print(not (A and not B) or (A or not C))
print(A and not B or not (A or not C))

# 6 version

A = True
B = False
C = True

print(not (A and B) and (not A or not C))
print(not (A and not B) or (A or not C))
print(A and not B or not (A or not C))

# 7 version

A = True
B = True
C = False

print(not (A and B) and (not A or not C))
print(not (A and not B) or (A or not C))
print(A and not B or not (A or not C))

# 8 version

A = False
B = False
C = True

print(not (A and B) and (not A or not C))
print(not (A and not B) or (A or not C))
print(A and not B or not (A or not C))