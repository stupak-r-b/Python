# ex. => 3.5.1
# find of perimeter of circle
import math

# 2*pi*r
print(str(math.pi * float(input())*2))



# ex. => 3.5.2
# write a program that starts from the console and
# prints the values of all the arguments passed to the screen
import sys

for i in sys.argv[1:]:
    print(i, end=" ")