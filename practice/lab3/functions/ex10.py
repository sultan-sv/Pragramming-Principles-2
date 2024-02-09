import operator
def filter(a):
    a = sorted(a)
    b = []
    for i in range(len(a)-1):
        if(a[i] == a[i+1]):
            continue
        else:
            b.append(a[i])
    print(b)
filter([1,1,1,2,2,3,3,2,2,4,3,1,4])
