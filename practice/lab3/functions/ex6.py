def ascii(s):
    int = 0
    a = []
    for i in range(len(s)):
        if(s[i] == " "):
            a.append(s[int:i+1])
            int = i+1
        elif(i == len(s) - 1):
            a.append(s[int:i+1])
    return a
s = input()
for i in range(len(ascii(s))):
    print((ascii(s)[len(ascii(s))-1-i]))

        
        