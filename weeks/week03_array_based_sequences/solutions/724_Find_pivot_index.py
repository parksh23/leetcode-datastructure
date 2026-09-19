class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_num = sum(nums)
        current_index = 0
        left_sum = 0
        while(current_index < len(nums)):
          if sum_num - left_sum - nums[current_index] == left_sum:
            return current_index
          left_sum += nums[current_index]
          current_index += 1

        return -1