class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        paren_dict = {'(' : ')', '[' : ']', '{' : '}'}
        for i in s:
          if i in "([{":
            stack.append(i)
          else:
            if len(stack) == 0 or i != paren_dict[stack.pop()]:
              return False

        return len(stack) == 0
        

if __name__ == "__main__":
  sol = Solution()
  result = sol.isValid("()(){}")
  print(f"결과 : {result}")