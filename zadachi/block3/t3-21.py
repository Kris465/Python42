num = [(True, True, True), (True, False, True), (True, True, False), (False, False, False), (False, True, False), (False, False, True), (False, True, True), (True, False, False)]
def compute_expressions(A, B, C):
    a = not (not A or not B and C)
    b = A and not (B and not C)
    c = not (not A or B and C)
    return a, b, C

for A, B, C in num:
    print(compute_expressions(A, B, C))
