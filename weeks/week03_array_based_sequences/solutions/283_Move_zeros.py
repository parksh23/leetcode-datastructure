class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        num_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[num_index] = nums[i]
                num_index += 1 
        
        if len(nums) > num_index:
            nums[num_index:] = [0] * (len(nums) - num_index)
        
        return nums