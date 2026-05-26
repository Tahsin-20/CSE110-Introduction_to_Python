password = input("Enter password: ")

upper = False
lower = False
digit = False
special = False

if len(password) >= 8:

    for ch in password:

        if (ch>='A' and ch<='Z'):
            upper = True

        elif (ch>='a' and ch<='z'):
            lower = True

        elif (ch>='0' and ch<='9'):
            digit = True

        elif (ch != ' '):
            special = True

if upper and lower and digit and special:
    print(True)
else:
    print(False)