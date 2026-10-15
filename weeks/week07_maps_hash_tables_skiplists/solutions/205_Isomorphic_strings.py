class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len_num = len(s)
        dict_s = dict()
        dict_t = dict()
        for i in range(len_num):
          if s[i] in dict_s and t[i] != dict_s[s[i]]:
            return False
          else:
            dict_s[s[i]] = t[i]

          if t[i] in dict_t and s[i] != dict_t[t[i]]:
            return False
          else:
            dict_t[t[i]] = s[i]

        return True