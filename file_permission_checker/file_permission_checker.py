import os
import stat
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
    print("Symbolic:",stat.filemode(os.stat(path).st_mode))
    if perm in ["777","767","666"]:
        print("[WARNING] File is world-writable and may pose a security risk")
else:
    print("invalid path")    