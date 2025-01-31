# а) не X и не Y;
# б) X или (не X и Y);
# в) (не X и Y) или Y.


#   Вариант 1

# x = True
# y = True


#   Вариант 2

# x = False
# y = True


#   Вариант 3

# x = True
# y = False


#   Вариант 4 

x = False
y = False


print(not x and not y)
print(x or (not x and y))
print((not x and y) or y)
