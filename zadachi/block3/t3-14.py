X = True
Y = True

result_a = not (X or Y)
result_b = not X and Y
result_c = X or not Y

print("""
Вычислить значение логического выражения при всех возможных значениях
логических величин X и Y:
а) не (X или Y);
б) не X и Y;
в) X и не Y.

Ответ:
      """)
print(f"A) {result_a}")
print(f"B) {result_b}")
print(f"C) {result_c}")
