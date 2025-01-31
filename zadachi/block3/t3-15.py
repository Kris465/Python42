# Вычислить значение логического выражения при всех возможных значениях 
# логических величин А и В:
# а) не А или не В;
# б) А и (А или не В);
# в) (не А или В) и В.

# Вариант_1

A = True
B = False

# а)
print(not A or not B)

# б)
print(A and (A or not B))

# в)
print((not A or B) and B)

# Вариант_2

A = True
B = True

# а)
print(not A or not B)

# б)
print(A and (A or not B))

# в)
print((not A or B) and B)

# Вариант_3

A = False
B = False

# а)
print(not A or not B)

# б)
print(A and (A or not B))

# в)
print((not A or B) and B)

# Вариант_4

A = False
B = True

# а)
print(not A or not B)

# б)
print(A and (A or not B))

# в)
print((not A or B) and B)
