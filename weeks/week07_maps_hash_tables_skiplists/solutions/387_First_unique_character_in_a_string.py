class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_dict = dict()
        for c in s:
          if c not in char_dict:
            char_dict[c] = 1
          else:
            char_dict[c] += 1

        for i, c in enumerate(s):
          if char_dict[c] == 1:
            return i

        return -1