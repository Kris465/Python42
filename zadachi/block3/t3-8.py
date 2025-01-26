# вычислить значение логического выражения при 
# следующих значениях логических 
# величин X, Y и Z: X = Ложь, Y = Истина, Z = Ложь:

# а) X и не (Z или Y) или не Z;
# б) не X или X и (Y или Z);
# в) (X или Y и не Z) и Z.

X = False
Y = True
Z = False

print(X or not (Z and Y) or not Z)
print(not X or X and (Y or Z))
print((X or Y and not Z) and Z)
