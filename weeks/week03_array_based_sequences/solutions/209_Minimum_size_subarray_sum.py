class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 1
        len_nums = len(nums)
        result = len_nums + 1
        if nums[0] >= target:
          return 1
        if len_nums == 1 and nums[0] < target:
          return 0

        sum_subs = nums[0] + nums[1]
        while(right >= left):
          if sum_subs < target:
            right += 1
            if right == len_nums : break
            sum_subs += nums[right]
          else :
            result = min(result, right - left + 1)
            sum_subs -= nums[left]
            left += 1

        if result != len_nums + 1:
          return result
        else : return 0
