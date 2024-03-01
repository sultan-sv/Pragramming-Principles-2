import re
def spl(string):
    return re.split('[A-Z]',string)
string = input()
print(spl(string))