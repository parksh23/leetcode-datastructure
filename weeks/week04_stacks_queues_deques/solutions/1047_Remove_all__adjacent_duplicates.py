class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_s = len(s)

        if len_s == 1:
          return s

        stack = []

        stack.append(s[0])

        for i in range(1, len_s):
          if stack and s[i] == stack[-1]:
            stack.pop()
          else:
            stack.append(s[i])

        return "".join(stack)
        