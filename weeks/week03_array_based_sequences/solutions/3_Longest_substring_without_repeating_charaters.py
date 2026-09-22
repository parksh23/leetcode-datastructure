class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right, len_s = 0, 1, len(s)
        if len_s <= 1:
          return len_s
        dict_s = dict()
        dict_s[s[0]] = 1
        current_len = 1
        answer = 0
        def function(left, right, current_len, answer):
          while(right >= left and right < len_s):
            temp = s[right]
            if temp not in dict_s or dict_s[temp] == 0:
              dict_s[temp] = 1
              right += 1
              current_len += 1
              answer = max(answer, current_len)
            else :
              dict_s[s[left]] -= 1
              left += 1
              current_len -= 1

          return answer


        return function(left, right, current_len, answer)

if __name__ == "__main__":
  sol = Solution()
  result = sol.lengthOfLongestSubstring("abcabcc")
  print(f"결과 : {result}")