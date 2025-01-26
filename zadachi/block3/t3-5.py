a = True
b = False
c = False

print((a or b and not c), (not a and not b), (not (a and c) or b), (
    a and not b or c), (a and (not b or c)), (a and (not (b and c))))
