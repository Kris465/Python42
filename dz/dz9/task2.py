count = 0

for number in range(100, 1000):
    digits = str(number)

    if (digits[0] == digits[1]) or \
            (digits[0] == digits[2]) or \
            (digits[1] == digits[2]):
        count += 1
        print(digits)

print(count)
