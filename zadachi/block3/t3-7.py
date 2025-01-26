# Вычислить значение логического выражения при следующих значениях логических
# величин А, В и С: А = Истина, В = Ложь, С = Ложь:

# а) А или не (А и В) или С;
# б) не А или А и (В или С);
# в) (А или В и не С) и С.

A = True
B = False
C = False

print(A or not (A and B) or C)
print(not A or A and (B or C))
print((A and B and not C) and C)
