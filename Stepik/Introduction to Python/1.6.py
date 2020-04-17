# ex. 1.6.1
# validation of password
password = input()
numbers = "1234567890"
for num in numbers:
    if num in password:
        if "1234" not in password and "qwerty" not in password and len(password) > 8:
            print("Good password")
            break
else:
    print("Bad password")