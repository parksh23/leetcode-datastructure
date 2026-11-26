import collections
import heapq

class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        frequent = collections.Counter(s)
        if max(frequent.values()) > (len(s) + 1) // 2:
          return ""

        max_heap = [(-cnt, num) for num, cnt in frequent.items()]
        heapq.heapify(max_heap)

        result = []

        while len(max_heap) >= 2:
          cnt1, char1 = heapq.heappop(max_heap)
          cnt2, char2 = heapq.heappop(max_heap)

          result.extend([char1, char2])

          if cnt1 + 1 < 0:
            heapq.heappush(max_heap, (cnt1 + 1, char1))
          if cnt2 + 1 < 0:
            heapq.heappush(max_heap, (cnt2 + 1, char2))
        
        if max_heap:
            result.append(max_heap[0][1])
            
        return "".join(result)