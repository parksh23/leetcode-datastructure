class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.max_len = k
        self.start = 0
        self.end = 0
        self.current_len = 0
        self.circulr_queue = [0] * k
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.current_len == self.max_len:
          return False
        self.circulr_queue[self.end] = value
        self.end = (self.end+1) % self.max_len
        self.current_len += 1
        return True
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.current_len == 0:
          return False
        self.start = (self.start + 1) % self.max_len
        self.current_len -= 1
        return True

    def Front(self):
        """
        :rtype: int
        """
        if self.current_len > 0:
          return self.circulr_queue[self.start]
        return -1
        

    def Rear(self):
        """
        :rtype: int
        """
        if self.current_len > 0:
          return self.circulr_queue[self.end - 1]
        return -1
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.current_len == 0
        

    def isFull(self):
        """
        :rtype: bool
        """
        return self.current_len == self.max_len
        