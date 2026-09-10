class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1

        if n == 1:
            return x

        if n < 0:
            x = 1.0 / x
            n = n * (-1)

        def recursion(x, n):
            if n == 1:
                return x

            if n % 2 == 0:
                return recursion(x, n/2) ** 2
            else:
                return (recursion(x, n/2) ** 2) * x
        
        return recursion(x, n)