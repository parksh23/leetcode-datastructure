import heapq

class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        n = len(points)
        min_heap = [(0, 0)]
        visited = set()
        cost_sum = 0

        while len(visited) < n:
          cost, curr = heapq.heappop(min_heap)

          if curr in visited:
            continue

          visited.add(curr)
          cost_sum += cost

          x1, y1 = points[curr]

          for next_node in range(n):
            if next_node not in visited:
              x2, y2 = points[next_node]
              dist = abs(x2 - x1) + abs(y2 - y1)
              heapq.heappush(min_heap, (dist, next_node))

        return cost_sum