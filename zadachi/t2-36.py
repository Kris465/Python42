num1 = input("введите трёхзначное число:")
num2  = input("введите двухзначное число:")

a1 = num1[0]
a2 = num1[1]
a3 = num1[2]

b1 = num2[0]
b2 = num2[1]
b3 = 0
l =  0

match b3:
    case"0":
        l = a3
    case"1":
        l = int(a3) + 1
    case"2":
        l = int(a3) + 2
    case"3":
        l = int(a3) + 3
    case"4":
        l = int(a3) + 4
    case"5":
        l = int(a3) + 5
    case"6":
        l = int(a3) + 6 
    case"7":
        l = int(a3) + 7
    case"8":
        l = int(a3) + 8
    case"9":
        l = int(a3) + 9

match b2:
    case"0":
        s = a2
    case"1":
        s = int(a2) + 1
    case"2":
        s = int(a2) + 2
    case"3":
        s = int(a2) + 3
    case"4":
        s = int(a2) + 4
    case"5":
        s = int(a2) + 5
    case"6":
        s = int(a2) + 6 
    case"7":
        s = int(a2) + 7
    case"8":
        s = int(a2) + 8
    case"9":
        s = int(a2) + 9 
    case _ :
        s = None


match b1:
    case"0":
        j = a1
    case"1":
        j = int(a1) + 1
    case"2":
        j = int(a1) + 2
    case"3":
        j = int(a1) + 3
    case"4":
        j = int(a1) + 4
    case"5":
        j = int(a1) + 5
    case"6":
        j = int(a1) + 6 
    case"7":
        j = int(a1) + 7
    case"8":
        j = int(a1) + 8
    case"9":
        j = int(a1) + 9 
    case _:
        j = None


print(f"Ответ: {str(j) + str(s) + str(l)}")
