import re
def camelToSnake(string):
    if(re.search('[A-Z]',string)):
        x = re.search('[A-Z]',string)[0]
        x = x.lower()
        string = re.sub('[A-Z]','_'+x,string,1)
        return camelToSnake(string)
    else:
        return string
string = input()
print(camelToSnake(string))
