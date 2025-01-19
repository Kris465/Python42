num1 = input("введите двузначное число:")
num2  = input("введите однозначоне число:")

a2 = num1[0]
a2 = num2[1]

match num2:
    case"0":
        s = a1
    case"1":
        s = int(a1) + 1
    case"2":
        s = int(a1) + 2
    case"3":
        s = int(a1) + 3
    case"4":
        s = int(a1) + 4
    case"5":
        s = int(a1) + 5
    case"6":
        s = int(a1) + 6 
    case"7":
        s = int(a1) + 7
    case"8":
        s = int(a1) + 8
    case"9":
        s = int(a1) + 9 
    case _ :
        s = None

  print(f"Ответ: {a2 + str (s)}")  

