import os
path = r'C:\Users\User\Desktop\Pragramming Principles 2\practice\lab6\directories_and_files'
if(os.access(path,os.F_OK)):
    for i in os.listdir(path):
        print(i)
else:
    print("file does not exist")

