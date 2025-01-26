
A = True
B = False
C = False

expression_a = not A and B
expression_b = A or not B
expression_c = A and B or C

print(f"Результат выражения ¬A ∧ B: {expression_a}")
print(f"Результат выражения A ∨ ¬B: {expression_b}")
print(f"Результат выражения A ∧ B ∨ C: {expression_c}")
