
X = True
Y = True
Z = False

expression_a = not X and Y
expression_b = X or not Y
expression_c = X or Y and Z

print(f"Результат выражения ¬X ∧ Y: {expression_a}")
print(f"Результат выражения X ∨ ¬Y: {expression_b}")
print(f"Результат выражения A ∧ Y ∨ Z: {expression_c}")
