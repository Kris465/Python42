# Вычислить значение логического выражения при всех возможных значениях 
# логических величин А и В:
# а) не (не А и не В) и А;
# б) не (не А или не В) или А;
# в) не (не А или не В) и В.

# version 1

A = False
B = False

print(not (not A and not B) and A)
print(not (not A or not B) or A)
print(not (not A or not B) and B)

# version 2

A = True
B = False

print(not (not A and not B) and A)
print(not (not A or not B) or A)
print(not (not A or not B) and B)

# version 3

A = False
B = True

print(not (not A and not B) and A)
print(not (not A or not B) or A)
print(not (not A or not B) and B)

# version 4

A = True
B = True

print(not (not A and not B) and A)
print(not (not A or not B) or A)
print(not (not A or not B) and B)
