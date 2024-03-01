import re
def test(string):
    newstring = ""
    for i in range(len(string)-1):
        if(string[i] != ' ' and string[i+1]>='A' and string[i+1]<='Z'):
            newstring += (string[i]+' ')
        else:
            newstring += string[i]
    newstring += string[len(string)-1]
    return newstring
string = input()
print(test(string))
            





