distance_from_home = 0
all_distance = 0
n = True

for i in range(1, 101):
    if n is True:
        all_distance += 1/i
        distance_from_home += 1/i
        n = False
    else:
        all_distance += 1/i
        distance_from_home -= 1/i
        n = True

print(f'Вся дистанция: {round(all_distance, 2)} км.')
print(f'Дистанция от дома: {round(distance_from_home, 2)} км.')
