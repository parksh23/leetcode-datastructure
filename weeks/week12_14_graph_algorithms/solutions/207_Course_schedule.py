class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
      neighbor_list = [[] for i in range(numCourses)]
      for start, end in prerequisites:
        neighbor_list[start].append(end)

      visited = [0 for _ in range(numCourses)]

      def dfs(node_num):
        if visited[node_num] == 2:
          return True

        if visited[node_num] == 1:
          return False

        visited[node_num] = 1
        for i in neighbor_list[node_num]:
          if not dfs(i):
            return False

        visited[node_num] = 2
        return True

      for j in range(numCourses):
        if not dfs(j): return False
      
      return True