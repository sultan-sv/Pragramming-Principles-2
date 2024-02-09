import math
def filter_prime(a):
    lis = []
    for j in range (len(a)):
        i = 2
        bool = True
        while i * i <= a[j]:
            if a[j] % i == 0:
                bool = False
            i = i + 1
        if(bool):
            lis.append(a[j])
    print(lis)
a = []
for i in range (100):
    a.append(i)    
filter_prime(a)