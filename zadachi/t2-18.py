num = int(input("Введите трехзначное число: "))
n1 = str(num // 100)
n2 = str((num // 10) % 10)
n3 = str(num % 10)
result1 = n1 + n3 + n2
result2 = n2 + n1 + n3
result3 = n3 + n1 + n2
result4 = n2 + n3 + n1
result5 = n3 + n1 + n2
result6 = n3 + n2 + n1
print(result1, result2, result3, result4, result5, result6)
