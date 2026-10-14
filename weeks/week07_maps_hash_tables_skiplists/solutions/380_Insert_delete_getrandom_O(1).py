class RandomizedSet(object):

    def __init__(self):
        self.num_list = []
        self.num_dict = dict()
        self.current = 0

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.num_dict:
          return False

        self.num_list.append(val)
        self.num_dict[val] = self.current
        self.current += 1

        return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.num_dict:
          return False

        if val == self.num_list[-1]:
          self.num_list.pop()
          del self.num_dict[val]
          self.current -= 1
          return True

        self.num_dict[self.num_list[-1]] = self.num_dict[val]
        temp = val
        self.num_list[self.num_dict[val]] = self.num_list[-1]
        self.num_list[-1] = temp
        del self.num_dict[val]
        self.num_list.pop()
        self.current -= 1
        return True

        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.num_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()