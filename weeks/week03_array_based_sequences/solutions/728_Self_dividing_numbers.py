class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def function(num):
          temp = num
          while(temp > 0):
            temp, digit = divmod(temp, 10)
            if digit == 0 or num % digit != 0:
              return False
          return True

        result = []
        for num in range(left, right + 1):
          if function(num):
            result.append(num)

        return result
