import collections
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_dict = collections.Counter(nums)

        min_heap = []

        for num, fre in num_dict.items():
          if len(min_heap) < k:
            heapq.heappush(min_heap, (fre, num))
          elif fre > min_heap[0][0]:
            heapq.heappushpop(min_heap, (fre, num))

        return [num for fre, num in min_heap]