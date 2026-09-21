class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_nums = sum(nums)
        len_nums = len(nums)
        set_nums = set()
        if sum_nums % 2 != 0:
            return False
        else :
            goal = sum_nums / 2
        set_nums.add(0)
        for num in nums:
            temp_set = set()
            for s in set_nums:
                if s + num == goal:
                    return True
                if s + num < goal:
                    temp_set.add(s + num)

            set_nums.update(temp_set)

        return False
