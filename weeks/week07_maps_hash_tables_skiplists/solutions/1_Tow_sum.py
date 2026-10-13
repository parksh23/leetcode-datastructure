class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        num_dict = dict()
        for i in range(len(nums)):
          if target - nums[i] not in num_dict:
            num_dict[nums[i]] = i

          else:
            return [num_dict[target - nums[i]], i]