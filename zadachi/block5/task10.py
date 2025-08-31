mon = 0
cors = 79.64
while True:
    an = round(mon * cors, 2)
    print(f"{mon}$ это - {an}Р")
    if mon == 20:
        break
    mon = mon + 1
