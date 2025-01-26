# числить значение логического выражения при следующих значениях
# логических величин X, Y и Z: X = Ложь, Y = Ложь, Z = Истина:
# а) X или Y и не Z; г) X и не Y или Z;
# б) не X и не Y; д) X и (не Y или Z);
# в) не (X и Z) или Y; е) X или (не (Y или Z))

x = False
y = False
z = True

print(x or y and not z)
print(not x and not y)
print(not (x and z) or y)
print(x and not y or z)
print(x and (not y or z))
print(x or (not (y or z)))
