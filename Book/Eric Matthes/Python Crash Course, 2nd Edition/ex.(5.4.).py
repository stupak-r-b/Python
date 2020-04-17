elien_color = "yellow"
score = 0

# if elien_color is green, the player earns 5 points
if elien_color == "green":
    score += 5
    print("You earned 5 points.")
else:
    score += 10
    print("You earned 10 points.")


# if elien_color is yellow, the player earns 10 points
if elien_color == "yellow":
    score += 10
    print("You earned 10 points")
else:
    score += 5
    print("You earned 5 points")
