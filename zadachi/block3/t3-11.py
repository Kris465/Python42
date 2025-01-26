# a)
x = 1
y = -1
if (x**2 + y**2 <= 4):
    print("True")
else:
    print("False")

# b)
x = 1
y = 2
if (x >= 0) or (y**2 != 4):
    print("False")
else:
    print("True")

# c)
x = 1
y = 2
if (x >= 0) and (y**2 != 4):
    print("False")
else:
    print("True")

# d)
x = 2
y = 1
if (x * y != 0) and (y > x):
    print("False")
else:
    print("True")

# e)
x = 2
y = 1
if (x * y != 0) or (y < x):
    print("True")
else:
    print("False")

# f)
x = 2
y = 1
if (not (x * y < 0)) and (y > x):
    print("False")
else:
    print("True")

# g)
x = 1
y = 2
if (not (x * y < 0)) or (y > x):
    print("True")
else:
    print("False")
