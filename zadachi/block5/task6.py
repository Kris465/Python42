# а

text_a = "21 20.4\n"
a_1 = 22
a_2 = 21

for i in range(14):
    text_a += f'{a_1} {a_2}.4\n'
    a_1 += 1
    a_2 += 1

print('Вариант А:\n')
print(text_a)


# б

text_b = "16 15.5 16.8\n"
b_1 = 17
b_2 = 16

for i in range(8):
    text_b += f'{b_1} {b_2}.5 {b_1}.8 \n'
    b_1 += 1
    b_2 += 1

print('Вариант Б:\n')
print(text_b)
