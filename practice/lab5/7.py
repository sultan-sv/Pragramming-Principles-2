import re
def snake_to_camel(string):
    str = '_[a-z]{1}'
    if(re.search(str,string)):
        x = re.search(str,string)[0]
        x = x.upper()
        string = re.sub(str,x[1],string,1)
        return snake_to_camel(string)
    else:
        return string
string = input()
print(snake_to_camel(string))
