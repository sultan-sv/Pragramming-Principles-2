import os
file = open('languages.txt','r')
file2 = open('languages2.txt','w') 
for i in range(len(file.readlines())):
    file2.write(file.readline())
