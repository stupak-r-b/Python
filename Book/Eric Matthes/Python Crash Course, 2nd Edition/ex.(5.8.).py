# make a list of five or more usernames, including the name 'admin'
usernames = ["admin", "guest232", "guest332", "gues444", "guest223"]

# loop through the list, and print a greeting to each user
for username in usernames:

# if the username is 'admin', print a special greeting
    if username == "admin":
        print("Hell admin, would you like to see a status report?")

# otherwise, print a generic greeting
    else:
        print(f"Hello {username}, thank you for logging in again")
