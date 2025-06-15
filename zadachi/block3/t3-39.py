h = int(input("введите часы: "))
m = int(input("введите минуты: "))
s = int(input("введите секунды: "))

if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
    h1 = 30
    m1 = 0.5
    s1 = 0.008333
    
    h = h * h1
    m = m * m1
    s = s * s1
    
    total = h + m + s
    
    print(f"в вашем случае стрелка в стольки градусах: {total}")