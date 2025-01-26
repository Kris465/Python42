A = True
B = False
C = False

print(not A or not B or not C)
print((not A or not B) or (A or B))
print(A and B or A and B or not C)
