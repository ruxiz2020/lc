from random import choice

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.hash_map = {}
        self.values = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """

        if val not in self.hash_map:
            self.hash_map[val] = len(self.values)
            self.values.append(val)

            return True

        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """

        if val in self.hash_map:
            index = self.hash_map[val]
            last_val = self.values.pop()
            if index < len(self.values):
                self.values[index] = last_val
                self.hash_map[last_val] = index
            del self.hash_map[val]

            return True

        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """

        return choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
