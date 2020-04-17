# make a lsit of five or more usernames called current_users
current_users = ["admin", "guest232", "guest332", "gues444", "guest223"]

# make a list of five usernames called new_users.
current_users = [user.lower() for user in current_users]
new_users = ["guest111", "guest232", "guest312", "gues444", "guest923"]

# loop through the new_users list to see if each new username has already been used.
for user in new_users:
    if user.lower() in current_users:
        print("You need to create another username.")
    else:
        print("Username created successfully.")
