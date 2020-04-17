# write a program that wil calculate the number of different objects in the list
objects = [1, 2, 1, 5, True, False, 'false', [], [1,2], [1,2]]
# add id of objects to a new list
objects_id = []
for i in objects:
    objects_id.append(id(i))
print(len(set(objects_id)))