import collections
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
      graph = collections.defaultdict(list)

      for u, v, w in times:
        graph[u].append((v, w))

      min_heap = [(0, k)]

      dist = {}

      while min_heap:
        current, next_node = heapq.heappop(min_heap)

        if next_node not in dist:
          dist[next_node] = current

          for v, w in graph[next_node]:
            if v not in dist:
              heapq.heappush(min_heap, (current + w, v))

      return max(dist.values()) if len(dist) == n else -1