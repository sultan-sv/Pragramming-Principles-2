import re
s = input()
def test(s):
    s = re.sub(' ',':',s)
    s = re.sub(r"\.",':',s)
    s = re.sub(',',':',s)
    return s
print(test(s))