g = int(input("введите год:"))
m = int(input("введите месяц:"))
n = int(input("введите число:"))
years = [12]
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#v1

if n > 1:
    n -= 1;
elif n == 1:
    n = 31
    m = 12
    n == month[m - 1];
else n == 1 and m == years
      g -= 1;
print( f"дата предыдущего дня {n}.{m}.{g}")

#v2

if n <= month[n + 1]:
    n += 1;
elif n == month:
    m += 1
    n = 1;
else n == month and m = years:
g += 1;
print(f"дата следующего дня {n}.{m}.{g}")
         
 