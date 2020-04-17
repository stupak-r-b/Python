# make a list of the numbers from one to one millon
list_of_num = [num for num in range(1, 1_000_001)]

# use min() and max() to make sure your list actually starts at one and ends at one millon
smallest = min(list_of_num)
largest = max(list_of_num)
print(smallest, largest)

# use sum() funtion to see how quickly Python can add a milion numbers
sum_of_million = sum(list_of_num)
print(sum_of_million)
