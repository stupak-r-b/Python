# ex. => 1.5.1
# create a MoneyBox class to work with a virtual piggy bank
class MoneyBox:

# the class must support information about the number of coins in the piggy bank
    def __init__(self, capacity = 100):
        self.capacity = capacity

# the class should provide an opportunity to find out whether it is possible to add some
# more coins to the piggy bank.
    def can_add(self, v):
        if self.capacity - v >= 0:
            return True
        return False

# the class should provide the ability to add coins to the piggy bank
    def add(self, v):
        if self.can_add(v):
            self.capacity -= v

# ex. => 1.5.2
#  you are given a sequence of integers and you need to process it and display the sum of the
# first five  from thes sequence, then the sum of the second five, etc.numbers
class Buffer:
    def __init__(self, some_list = []):
        self.some_list = some_list

    def add(self, *a):
        self.some_list += [*a]
        if len(self.some_list) >= 5:
            while len(self.some_list) >= 5:
                print(sum(self.some_list[0:5]))
                del self.some_list[0:5]

    def get_current_part(self):
        return self.some_list