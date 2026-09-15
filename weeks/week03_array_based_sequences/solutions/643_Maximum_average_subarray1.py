class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        len_nums = len(nums)

        first_sum = sum(nums[:k])
        result = first_sum
        for i in range(1, len_nums - k + 1):
          first_sum -= nums[i - 1]
          first_sum += nums[k + i - 1]
          result = max(result, first_sum)

        return result / float(k)