import os
from collections import defaultdict
path=input("Enter file path:")
if not os.path.isfile(path):
            print("File do not exist")
else:
    with open("report.txt","w") as report:
        with open(path,"r") as log:
                lines_count=0
                error_count=0
                warning_count=0
                info_count=0
                for  line in log:
                        lines_count+=1
                        if "error" in line.lower():
                                error_count+=1
                        elif "warning" in line.lower():
                                warning_count+=1
                        elif "info" in line.lower():
                                info_count+=1
                print(f"total lines:{lines_count}")
                print(f"total Error messages:{error_count}")
                print(f"total Warning messages:{warning_count}")
                print(f"total Info messages:{info_count}")
                print("-"*50)
                report.write("="*10+"SECURITY REPORT"+"="*10)
                report.write(f"\nTotal Lines :{lines_count}\n")
                report.write(f"ERROR       :{error_count}\n")
                report.write(f"WARNING     :{warning_count}\n")
                report.write(f"INFO        :{info_count}\n")
                            
        with open(path,"r") as log:      
                keyword=input("Enter keyword to search:")
                found=[]
                for line in log:
                        if keyword.lower() in line.lower():
                                found.append(line)
                if found:
                    print(f"Found {len(found)} matching lines:")
                    report.write("\nKeyword Search\n")
                    report.write("-"*30)
                    report.write(f"\nKeyword: {keyword}\n")
                    report.write(f"Matches: {len(found)}\n")
                    for line in found:
                        print(line)
                else:
                        print("Found 0 matching lines.")
                        report.write("\nKeyword Search\n")
                        report.write("-" * 30)
                        report.write(f"\nKeyword: {keyword}\n")
                        report.write("Matches: 0\n")
        with open(path,"r") as log:
                ips=defaultdict(int)
                for line in log:
                        if "failed password" in line.lower():
                                parts=line.split()
                                index=parts.index("from")
                                ips[parts[index+1]]+=1
                report.write("\nFailed Login Attempts\n")
                report.write("-"*30+"\n")
                print("Failed Login Attempts by IP:")
                for key,val in ips.items():
                        print(f"{key} : {val}")
                        report.write(f"{key} : {val}\n")
    print("\nSecurity report saved as report.txt")
