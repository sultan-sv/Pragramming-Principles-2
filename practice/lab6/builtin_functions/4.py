import time
import math
def square(mil,number):
    time.sleep(mil/1000)
    print(math.sqrt(number))
string = input()
a = []
counter = 0
for i in range(len(string)):
    if(string[i] == " "):
        a.append(string[counter:i])
        counter = i+1
a.append(string[counter:len(string)])
square(int(a[1]),int(a[0]))

