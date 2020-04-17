# verification of conditions

name = "Michael"

if name == "Michael":
    print(f"Yes, his name is {name}")
if name == "michael".title():
    print(f"Yes, his name is {name}")


name = "ronald"

if name != "Michael":
    print(f"His name isn't Michael, his name is {name.title()}")
if name == "Ronald".lower():
    print(f"His name is {name.title()}")

number = 44
if 23 < number < 45:
    print("True")
if number > 35 and number > 40:
    print("True")

nums = [1, 2, 3, 4, 5, 5, 6, 7]
if 34 in nums:
    print("True")
else:
    print("False")
