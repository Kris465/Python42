def is_lucky_ticket(number):
    num_str = str(number)


    if len(num_str) !=6:
        return False


    left_part = num_str[:3]
    right_part = num_str[3:]

    sum_left = sum(int(digit) for digit in left_part)
    sum_right = sum(int(digit) for digit in right_part)

    return sum_left == sum_right


ticket = 123420
print(is_lucky_ticket(ticket))
