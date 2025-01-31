#  Вычислить значение логического выражения при всех возможных значениях 
# логических величин А и В:

# а) не А и не В или А;
# б) В или не А и не В;
# в) В и не (А и не В).

# 1

a = True
b = True

print(not a and not b or a)
print(b or not a and not b)
print(b and not (a and not b))

# 2

a = False
b = False

print(not a and not b or a)
print(b or not a and not b)
print(b and not (a and not b))

# 3

a = True
b = False

print(not a and not b or a)
print(b or not a and not b)
print(b and not (a and not b))

# 4

a = False
b = True

print(not a and not b or a)
print(b or not a and not b)
print(b and not (a and not b))
