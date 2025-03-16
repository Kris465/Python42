let x = Number(prompt('Введите число для первой переменной: '))
let y = Number(prompt('Введите число для второй переменной: '))
let dividend = (x + ((2 + y) / (x * x)))
let divider = y + (1 / Math.sqrt(x * x + 10))
let result_1 = alert(`Ответ: ${(dividend / divider)}`)
let result_2 = 2.8*Math.sin(x) + 