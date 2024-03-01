import re
s = input()
str = 'a(b*)'
x = re.search(str,s)
print(x)
if x:
    print("found")
else:
    print("not found")
