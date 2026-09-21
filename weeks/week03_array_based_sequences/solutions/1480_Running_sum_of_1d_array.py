class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        len_nums = len(nums)
        for i in range(1, len_nums):
          nums[i] = nums[i-1] + nums[i]

        return nums
        