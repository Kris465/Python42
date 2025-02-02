import itertools
values = [True, False]
for A, B, C in itertools.product(values, repeat=3):
    
    result_a = not (A or (not B and C)) or C
 
    result_b = not (A and (not B or C)) and B
 
    result_c = not (not A or (B and C)) or A
    
    print(f"A: {A}, B: {B}, C: {C} => "
          f"Result A: {result_a}, "
          f"Result B: {result_b}, "
          f"Result C: {result_c}")

