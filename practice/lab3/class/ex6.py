import math
def filter(a):
    b = []
    for i in a:
        bool = True
        for j in range(2,round(math.sqrt(i))+1):
            if(i%j == 0):
                bool = False
        if (bool):
            b.append(i)
    return b
x = []
for i in range(1,1000):
    x.append(i)
y = lambda x:filter(x)
print(y(x))