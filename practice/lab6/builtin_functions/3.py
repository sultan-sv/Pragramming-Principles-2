def palindrome(string):
    bol = True
    for i in range(len(string)//2):
        if(string[i] == string[len(string)-i-1]):
            bol = True
        else:
            bol = False
            break
    return bol
string = input()
if(palindrome(string)):
    print("yes")
else:
    print("no")

# pal2(string):
    #return string == string[::-1]

# def pal3(string):
#     rev = ''.join(reversed(string))
#     return string == rev