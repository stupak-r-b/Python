# Alex usually sleeps at night for X hours and rests Y minutes in the afternoon.
# Count how many minutes Alex sleeps per day.
X = int(input())
Y = int(input())
print(X * 60 + Y)           # if X = 7 and Y = 30   answer => 450

# convert minutes to standard time display
X = int(input())
hour = X // 60
minute =  X % 60
print(hour)
print(minute)               # if X = 480    answer => 8 h 0 min

# sum hour, minutes and convert to standard time display
X = int(input())
H = int(input())
M = int(input())
hour = X // 60 + H
minute =  X % 60 + M
if minute > 60:
    minute -= 60
    hour += 1

print(hour)
print(minute)