elien_color = "yellow"
score = 0

# if the alien is green, print a message that the player earned 5 points
if elien_color == "green":
    score += 5
    print("You earned 5 points.")

# if the alien is yellow, print a message that the player earned 10 points.
elif elien_color == "yellow":
    score += 10
    print("You earned 10 points.")

# if the alien is red, print a message that the player earned 15 prints.
else:
    score += 15
    print("You earned 15 points.")
