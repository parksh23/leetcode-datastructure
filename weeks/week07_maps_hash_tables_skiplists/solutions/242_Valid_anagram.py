class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_len, t_len = len(s), len(t)
        dict_s = dict()
        dict_t = dict()
        if s_len != t_len:
          return False

        for i in range(s_len):
          dict_s[s[i]] = dict_s.get(s[i], 0) + 1
          dict_t[t[i]] = dict_t.get(t[i], 0) + 1

        return dict_s == dict_t