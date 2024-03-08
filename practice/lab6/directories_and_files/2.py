import os
path = r'C:\Users\User\Desktop\Pragramming Principles 2\practice\lab6\directories_and_files'
print("Exist:", os.access(path, os.F_OK))
print("Readable:", os.access(path, os.R_OK))
print("Writable:", os.access(path, os.W_OK))
print("Executable:", os.access(path, os.X_OK))

