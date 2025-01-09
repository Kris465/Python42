def count_numbers():
    count = 0
    for num in range(100, 10000):
        if len(set(str(num))) == len(str(num)):
            count += 1
            # print(num)
    return count


result = count_numbers()
print(f"Количество чисел: {result}")
