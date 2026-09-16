class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        left, right = 0, len(nums)-1
        
        def recursion(left, right):
          if left == right:
            return nums[left]

          left_result = nums[left] - recursion(left+1, right)
          right_result = nums[right] - recursion(left, right-1)

          if left_result >= right_result:
            return left_result
          else:
            return right_result

        return recursion(left, right) >= 0
