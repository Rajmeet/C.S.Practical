import re

username = input("Enter your username: ")
password = input("Enter your password: ")

x = True

while x:
    if(len(password) < 6 or len(password) > 20):
        break
    elif not re.search("[a-z]", password):
        break
    elif not re.search("[0-9]", password):
        break
    elif not re.search("[A-Z]", password):
        break
    elif not re.search("[$#@]", password):
        break
    else:
        print("Valid Password", password)
        x = False
        break

if x:
    print("Not a Valid Password")