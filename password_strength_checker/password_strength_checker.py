import re
def password_strength(pwd):
    score = 0
    issues=[]
    mandatory_length_flag=False
    if len(pwd)<12:
        issues.append("length cannot be less than 12")
    else:
        mandatory_length_flag=True
        score += 1
    if re.search(r"[a-z]",pwd):
        score += 1
    else:
        issues.append("Missing lower characters")
    if re.search(r"[A-Z]",pwd):
        score += 1
    else:
        issues.append("Missing upper characters")
    if re.search(r"[0-9]",pwd):
        score += 1
    else:
        issues.append("Missing digits")
    if re.search(r"[^a-zA-Z0-9]",pwd):
        score += 1
    else:
        issues.append("Missing special characters")
    if(mandatory_length_flag):
        return score,issues
    else:
        return 0,issues
    
if __name__ == "__main__":
    password = input("enter your password:")
    score , problems = password_strength(password)
    if score <= 2 :
        print("weak password!")
        for issue in problems:
            print(issue)
    elif score <= 3 :
        print("medium password")
        for issue in problems:
            print(issue)
    else:
        print("strong password!")