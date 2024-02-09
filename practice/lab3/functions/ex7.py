def test(a):
    for i in range(len(a)-1):
        bool = False
        if(a[i] == 3 and a[i+1] == 3):
            bool = True
    if(bool == True):
        print("True")
    else:
        print("False")
b = int(input())
a = []
for i in range (b):
    c = int(input())
    a.append(c)
test(a)
        

