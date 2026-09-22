class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0 :
          return [n]
        if n == 1 :
          return [0, 1]
        answer = [0, 1]
        for i in range(2, n + 1):
          answer.append(answer[i >> 1] + (i & 1))
        return answer
