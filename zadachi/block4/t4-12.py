# Известны сопротивления двух несоединенных друг с другом участков элек
# трической цепи и напряжение на каждом из них. По какому участку протекает 
# меньший ток?

R1 = 4
R2 = 3
U1 = 12
U2 = 9

def compare_chisla(U1, R1, U2, R2):
    I1 = U1 / R1
    I2 = U2 / R2
    
    if I1 < I2:
        return 1
    elif I1 > I2:
        return 2
    else:
        return 0
    
result = compare_chisla(U1, R1, U2, R2)
    
if result == 0:
    print("Токи равны")
else:
    print(f"Меньший ток находится {result}.")

# хз где ошибка...