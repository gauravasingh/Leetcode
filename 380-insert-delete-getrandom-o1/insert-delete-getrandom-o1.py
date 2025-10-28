import random

class RandomizedSet(object):

    def __init__(self):
        """Initialize the data structure."""
        self.map = {}  # val -> index in list
        self.list = []  # store values

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            return False
        self.map[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.map:
            return False

        # Get index of element to remove
        idx = self.map[val]
        last_val = self.list[-1]

        # Move last element to idx
        self.list[idx] = last_val
        self.map[last_val] = idx

        # Remove last element
        self.list.pop()
        del self.map[val]

        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()