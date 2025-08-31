import math


def calculate_horizont_distance(height_km, radius_km=6350):
    height_m = height_km * 1000
    radius_m = radius_km * 1000

    distance_m = math.sqrt(2 * radius_m * height_m + height_m**2)

    return distance_m / 1000


for height in range(1, 11):
    distance = calculate_horizont_distance(height)
    print(f'Высота {height:6}(км)   -   Расстояние до горизонта {distance:22.3f}')
