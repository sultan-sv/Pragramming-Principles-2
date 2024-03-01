import re
def test(string):
    str = 'a.+b$'
    return re.search(str,string)[0]
string = input()
print(test(string))