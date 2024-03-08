import math
string = input()
counter1 = 0
counter2 = 0
for i in string:
    if i.islower():
        counter1 += 1
    elif i.isupper():
        counter2 += 1
print(counter1)
print(counter2)