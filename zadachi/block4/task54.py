def can_fit(suitcase, box):
    suitcase_sorted = sorted(suitcase)
    box_sorted = sorted(box)

    return all(box_dim <= suitcase_dim for box_dim, suitcase_dim in zip(box_sorted, suitcase_sorted))

a1, a2, a3 = map(int, input("Введите размеры чемодана (a1 a2 a3): ").split())
b1, b2, b3 = map(int, input("Введите размеры коробки (b1 b2 b3): ").split())

if can_fit((a1, a2, a3), (b1, b2, b3)):
    print("Коробка может поместиться в чемодан.")
else:
    print("Коробка не может поместиться в чемодан.")
