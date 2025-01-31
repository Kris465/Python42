x = False
y = False

print(not (not x and not y) and x)
print(not (not x or not y) or x)
print(not (not x or not y) and y)

# version 2

x = True
y = False
print(not (not x and not y) and x)
print(not (not x or not y) or x)
print(not (not x or not y) and y)

# version 3

x = False
y = True

print(not (not x and not y) and x)
print(not (not x or not y) or x)
print(not (not x or not y) and y)

# version 4

x = True
y = True

print(not (not x and not y) and x)
print(not (not x or not y) or x)
print(not (not x or not y) and y)
