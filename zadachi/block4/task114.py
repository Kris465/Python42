g = int(input("введите год:"))
m = int(input("введите месяц:"))
n = int(input("введите число:"))  

match g:
    case 1:
        if n >= 31:
            print(f"{1}.{m + 1}.{g}")
            print(f"{n - 1}.{m}.{g}")
            
    case 2:
        if n >= 30:
            print(f"{1}.{m + 1}.{g}")
            print(f"{n - 1}.{m}.{g}")
            
    case 3:
        if n >= 29:
            print(f"{1}.{m + 1}.{g}")
            print(f"{n - 1}.{m}.{g}")
            
    case 4:
        if n >= 31 and m >= 12:
            print(f"{1}.{1}.{g + 1}")
            print(f"{n - 1}.{m}.{g}")
    case 5:
        if n == 1:
            print(f"{n + 1}.{m}.{g}")
            print(f"{31}.{m - 1}.{g}")
    case 6:
        if n == 1 and m == 1:
            print(f"{n + 1}.{m}.{g}")
            print(f"{31}.{12}.{g - 1}")
        else:
            print(f"{n + 1}.{m}.{g}")
            print(f"{n - 1}.{m}.{g}")


# if n >= 30:
#     print(f"{g , m + 1} 1")
#     print(f"{g, m, n - 1} ")
# elif m >= 12 and n >= 30 :
#     print(f"{g + 1} {m} {n}")
#     print(f"{g, m, n - 1}")
# else:
#     print(f"{g, m, n + 1}")
    