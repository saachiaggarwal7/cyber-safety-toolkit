import os
path=input("enter path:")
if os.path.exists(path):
    if os.path.isfile(path):
        print ("Type:     File")
    elif os.path.isdir(path):
        print ("Type:     Directory")
    print("Read:        ",os.access(path,os.R_OK))
    print("Write:       ",os.access(path,os.W_OK))
    print("Execute:     ",os.access(path,os.X_OK))
    perm=oct(os.stat(path).st_mode)[-3:]
    print("Permissions: ",perm)
else:
    print("invalid path")