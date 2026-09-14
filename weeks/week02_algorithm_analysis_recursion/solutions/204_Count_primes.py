class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        def is_prime(m):
          answer = []
          
          if n <= 2:
              return 0
            
          TF_array = [True] * (n)
          TF_array[0] = False
          TF_array[1] = False
          tries = int(pow(n, 0.5)) + 1

          for i in range(2, tries):
            if TF_array[i]:
              TF_array[i*i : n : i] = [False] * (((n - 1 - i*i) // i) + 1)

          return sum(TF_array)

        return is_prime(n)