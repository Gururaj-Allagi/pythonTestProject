import re

regEx = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

def checkEmail(Email):
    if re.search(regEx, Email):
        print("valid")
    else:
        print("invalid")

checkEmail("gsa943@gmailcom")

email = "gsa943@gmail.in"
if ("@" in email) & (".com" in email) | (".in" in email):
    print("pass")