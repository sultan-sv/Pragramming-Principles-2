path = r'C:\Users\User\Desktop\Pragramming Principles 2\practice\lab6\directories_and_files'
import os
if(os.access(path,os.F_OK)):
        os.remove('erase.txt')
else:
    print('file does not exist')