class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.k = k
        self.my_deque = [0] * k
        self.start = 0
        self.rear = 0
        self.current_len = 0
        

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.current_len == self.k:
          return False
        self.start = (self.start+self.k-1) % self.k
        self.my_deque[self.start] = value
        self.current_len += 1
        return True
        

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.current_len == self.k:
          return False
        self.my_deque[self.rear] = value
        self.rear = (self.rear+1) % self.k
        self.current_len += 1
        return True
        

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.current_len == 0:
          return False
        self.start = (self.start+1) % self.k
        self.current_len -= 1
        return True
        

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.current_len == 0:
          return False
        self.rear = (self.rear+self.k-1) % self.k
        self.current_len -= 1
        return True
        

    def getFront(self):
        """
        :rtype: int
        """
        if self.current_len == 0:
          return -1
        return self.my_deque[self.start]
        

    def getRear(self):
        """
        :rtype: int
        """
        if self.current_len == 0:
          return -1
        return self.my_deque[(self.rear+self.k-1) % self.k]
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.current_len == 0
        

    def isFull(self):
        """
        :rtype: bool
        """
        return self.current_len == self.k
        