import math
height = int(input('height: '))
base1 = int(input('base1: '))
base2 = int(input('base2: '))
if(base1>base2):
    area = (base1 - base2)*height/2 + height*base2
else:
    area = (base2 - base1)*height/2 + height*base1
print(area)