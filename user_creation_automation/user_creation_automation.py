import subprocess
import getpass

username=input("enter username:")
result=subprocess.run(["id",username],capture_output=True,text=True)
if result.returncode==0:
        print("User already exists")
else:
        result=subprocess.run(["sudo","useradd","-m",username],capture_output=True,text=True)
        if result.returncode!=0:
                print("User not created")
                print(result.stderr)
        else:
                print("User created successfully.")
                password=getpass.getpass("Enter password:")
                password_data=f"{username}:{password}"
                result=subprocess.run(["sudo","chpasswd"],input=password_data,text=True,capture_output=True)
                if result.returncode!=0:
                        print("Failed to set password.")
                        print(result.stderr)
                else:
                        print("password set successfully.")
                        print("Add user to a group?")
                        print("1. sudo")
                        print("2. developers")
                        print("3. users")
                        print("4. Skip")
                        try:
                                choice=int(input("enter your choice:"))
                        except ValueError:
                                print("please enter a number between 1 and 4")
                                exit()
                        if choice==1:
                                result=subprocess.run(["sudo","usermod","-aG","sudo",username],capture_output=True,text=True)
                                if result.returncode!=0:
                                  print("Failed to add user to sudo group.")
                                  print(result.stderr)    
                                else:
                                  print("user added to sudo group successfully.")
                        elif choice==2:
                                result=subprocess.run(["sudo","usermod","-aG","developers",username],capture_output=True,text=True)
                                if result.returncode!=0:
                                  print("Failed to add user to developers group.")
                                  print(result.stderr)    
                                else:
                                  print("user added to developers group successfully.")
                        elif choice==3:
                                result=subprocess.run(["sudo","usermod","-aG","users",username],capture_output=True,text=True)
                                if result.returncode!=0:
                                  print("Failed to add user to users group.")
                                  print(result.stderr)    
                                else:
                                  print("user added to users group successfully.")
                        elif choice==4:
                                pass
                        else:
                                print("invalid choice!")
