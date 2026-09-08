class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)
  

if __name__ == "__main__":
    sol = Solution()
    # n에 원하는 숫자를 넣어서 테스트 (예: 5)
    result = sol.fib(5) 
    print(f"fib(5)의 결과: {result}")