class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0
        for i in range(len(nums)):
            answer ^= i + 1
            answer ^= nums[i]

        return answer

        