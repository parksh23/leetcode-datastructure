class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set()
        
        for num in nums:
            if num in num_set:
                num_set.remove(num)
            else:
                num_set.add(num)
        
        return num_set.pop()
        