X = True
Y = False
Z = False

print(not X or not Y or not Z)
print((not X or not Y) or (X or Y))
print(X and Y or X and Z or not Z)
