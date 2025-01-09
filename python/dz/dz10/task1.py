def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def print_primes_in_range(start, end):
    print(f"Простые числа в диапазоне от {start} до {end}:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=' ')
    print()


start_range = int(input("Введите начальное число диапазона: "))
end_range = int(input("Введите конечное число диапазона: "))
print_primes_in_range(start_range, end_range)
