import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
          return 0

        row, col = len(grid), len(grid[0])

        island = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(start_r : int, start_c : int):
          queue = collections.deque([(start_r, start_c)])
          grid[start_r][start_c] = "0"

          while queue:
            r, c = queue.popleft()

            for x, y in directions:
              nr, nc = r + x, c + y

              if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == "1":
                grid[nr][nc] = "0"
                queue.append((nr, nc))

        for r in range(row):
          for c in range(col):
            if grid[r][c] == "1":
              island += 1
              bfs(r, c)

        return island