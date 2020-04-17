# write a function that accepts a size and the thext of a message that should be printed on the shirt
def make_shirt(size, message):
    return f"You choose {size} size, and the message on the shirt is '{message}'"

print(make_shirt(size="L", message="ReEx"))