import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_heap = []

        for num in nums:
          if len(min_heap) < k:
            heapq.heappush(min_heap, num)
          elif num > min_heap[0]:
            heapq.heappushpop(min_heap, num)

        return min_heap[0]