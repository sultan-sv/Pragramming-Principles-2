import re
def test(string):
    str = "[A-Z]{1}[a-z]+"
    string = re.findall(str,string)
    return string
s = input()
print(test(s))