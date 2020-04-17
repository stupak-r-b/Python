# create a list with five usernames
usernames = ["admin", "guest232", "guest332", "gues444", "guest223"]

if usernames:
    for username in usernames:
        if username == "admin":
            print("Hell admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again")

# if the list is empty, print the message "We need to find some users!"
else:
    print("We need to ind some users!")
