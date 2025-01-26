X = False
Y = True
Z = False

print(X or not (Z and Y) or not Z)
print(not X or X and (Y or Z))
print((X or Y and not Z) and Z)
