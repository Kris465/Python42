# Из трехзначного числа x вычли его последнюю цифру.
# Когда результат разде-лили на 10,
# а к частному слева приписали последнюю цифру числа x,
# то полу-чилось число 237
# Найти число x.

# Step_1
a = '237'
a = a.replace('2', '')

# Step_2
a = int(a)*10

# Step_3
a = str(a)
a = a.replace('0', '2')
print(a)
