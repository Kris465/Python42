
# a)
X1 = 27
Y1 = 46

if X1 % 2 and Y1 % 2:
    print(True)
    
# б)
X2 = 51
Y2 = 1

if X2 < 50 or Y2 < 50:
    print(True)
    
# в)
X3 = 27
Y3 = 0
if X3 == 0 or Y3 == 0:
    print(True)
    
# г)
X4 = -27
Y4 = -1
Z4 = -105
if X4 < 0 and Y4 < 0 and Z4 < 0:
    print(True)
    
# д)
X5 = 27
Y5 = 1
Z5 = 105
if X5 // 5 or Y5 // 5 or Z5 // 5:
    print(True)
    
# е)
X6 = 27
Y6 = 0
Z6 = 105
if X6 > 100 or Y6 > 100 or Z6 > 100:
    print(True)

else:
    print(False)