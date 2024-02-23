import math
sides = int(input("input the number of sides "))
length = int(input("input the length of the side "))
angle = 360/(sides)/(180/math.pi)
length2 = length/(2*math.tan(angle/2))
area = (length/2)*length2*sides
print(area)