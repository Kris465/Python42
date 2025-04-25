material1_massa = int(input('Введите массу первого материала: '))
material1_ob = int(input('Введите объем первого материала: '))
material2_massa = int(input('Введите массу второго материала: '))
material2_ob = int(input('Введите объем второго материала: '))
plotnost = material1_massa // material1_ob
plotnost2 = material2_massa // material2_ob
if plotnost > plotnost2:
    print("Плотность первого объекта больше второго")
elif plotnost < plotnost2:
    print("Плотность второго объекта больше первго")
else:
    print("Плотнось первго и плотность второго равны")
