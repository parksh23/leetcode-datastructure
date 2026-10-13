class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        front = 0
        end = len(numbers) - 1

        while(True):
          front_num = numbers[front]
          end_num = numbers[end]
          if front_num + end_num == target:
            return [front+1, end+1]

          elif front_num + end_num > target:
            end -= 1

          else:
            front += 1
