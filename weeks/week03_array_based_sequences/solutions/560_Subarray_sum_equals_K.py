class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        len_nums = len(nums)
        dict_sub = dict()
        sum_nums = 0
        result = 0
        for i in range(len_nums):
          sum_nums += nums[i]
          if sum_nums - k ==0:
            result += 1
          if sum_nums - k in dict_sub:
            result += dict_sub[sum_nums - k]
          if sum_nums in dict_sub:
            dict_sub[sum_nums] += 1
          else : dict_sub[sum_nums] = 1
        
        return result
        