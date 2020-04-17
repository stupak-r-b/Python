# ex. => 1.3.1
# write the function that tales the integer x as the only argument and returns the smallest integer y:
# and y must be greater or equal to x, and y should be divisible by 5
def closest_mod_5(x):
    if x % 5 == 0: return  x
    while True:
        x += 1
        if x % 5 == 0: return x