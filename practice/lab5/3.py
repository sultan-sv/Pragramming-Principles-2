import re
def test(string):
    str = "([a-z]+_+[a-z]+_+)+[a-z]+"
    x = re.search(str,string)
    return x[0]
s = input()
print(test(s))
