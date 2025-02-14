x = True
y = False
z = False

print(not (x and y) and (not x or not z))
print(not (x and not y) or (x or not z))
print(x and not y or not (x or not z))


#version №2
x = False
y = True
z = True

print(not (x and y) and (not x or not z))
print(not (x and not y) or (x or not z))
print(x and not y or not (x or not z))