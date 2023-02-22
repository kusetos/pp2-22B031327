import math
#print(help(math))
# from degree to rad 1
print(math.radians(15))

# area of trapezoid 2
"""height = int(input())
firstVal = int(input())
secondVal = int(input())"""
height = 5
firstVal =5
secondVal =6
print(((firstVal + secondVal) / 2) * height)

# regular polygon 3
"""
Sides = int(input())
lengthSide = int(input())
"""
Sides = 4
lengthSide = 25
P = Sides * lengthSide
a = (lengthSide/ (2 * math.tanh(180/Sides)))
area = P /2 * a
print(area)

# parallelogram 4
base = 5
height = 6
print(base * height)
