def find_bounding_rectangle(rect1, rect2):  
    x1, y1, width1, height1 = rect1
    x1_max = x1 + width1
    y1_max = y1 + height1

    x2, y2, width2, height2 = rect2
    x2_max = x2 + width2
    y2_max = y2 + height2

    min_x = min(x1, x2)
    min_y = min(y1, y2)

    max_x = max(x1_max, x2_max)
    max_y = max(y1_max, y2_max)

    return (min_x, min_y), (max_x, max_y) 

rect1 = (0, 0, 3, 4)
rect2 = (2, 3, 5, 6)

bottom_left_corner, top_right_corner = find_bounding_rectangle(rect1, rect2)
print("левый нижний уол", bottom_left_corner)
print("правый верхний угол:", top_right_corner)
