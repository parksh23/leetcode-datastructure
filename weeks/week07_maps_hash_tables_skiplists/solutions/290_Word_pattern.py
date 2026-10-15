class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        dict_patt = dict()
        dict_word = dict()
        words = s.split()

        if len(pattern) != len(words):
            return False

        for p, c in zip(pattern, words):
          if p in dict_patt and dict_patt[p] != c:
            return False
          if c in dict_word and dict_word[c] != p:
            return False

          dict_patt[p] = c
          dict_word[c] = p

        return True