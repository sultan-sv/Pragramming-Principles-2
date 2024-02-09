def zzs(a):
    bool = False
    for i in range(len(a)-2):
        if(a[i] == 0 and a[i+1] == 0 and a[i+2] == 7):
            bool = True
    return bool
print(zzs([7,0,0,0]))
