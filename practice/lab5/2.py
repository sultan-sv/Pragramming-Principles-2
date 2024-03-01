import re
def test(string):
    str = "a(b{2,3})"
    if(re.search(str,string)):
        return True
    else:
        return False
s = input()
if(test(s)):
    print("found")
else:
    print("not found")
