import os
import shutil
from datetime import datetime

file_path=input("Enter the file path:")
if not os.path.isfile(file_path):
    print("Invalid file path.")
else:
    file_name=os.path.basename(file_path)
    name,extension=os.path.splitext(file_name)
    if not os.path.exists("backups"):
        os.mkdir("backups")
    timestamp=datetime.now().strftime("%Y%m%d_%H%M%S")
    log_time=datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
    new_filename=f"{name}_{timestamp}{extension}"
    new_path=os.path.join("backups",new_filename)
    shutil.copy2(file_path,new_path)
    print(f"Backup created successfully: {new_path}")
    with open("backup.log","a") as file:
        file.write(f"""
{log_time}
Original:{file_path}
Backup:{new_path}
{'-'*40}
""")
    
