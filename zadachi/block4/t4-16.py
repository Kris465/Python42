import math

def can_circle_fit_in_square(circle_radius, square_side):
    circle_diameter = 2 * circle_radius
    return circle_diameter <= square_side

def can_square_fit_in_circle(circle_radius, square_side):
    square_diagonal = square_side * math.sqrt(2)
    circle_diameter = 2 * circle_radius
    return square_diagonal <= circle_diameter

circle_radius = float(input("Введите радиус круга: "))
square_side = float(input("Введите длину стороны квадрата: "))

if can_circle_fit_in_square(circle_radius, square_side):
    print("Круг уместится в квадрате.")
else:
    print("Круг не уместится в квадрате.")

if can_square_fit_in_circle(circle_radius, square_side):
    print("Квадрат уместится в круге.")
else:
    print("Квадрат не уместится в круге.")