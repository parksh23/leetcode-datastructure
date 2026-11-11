class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        queue = deque([0])
        visited = {0}

        while queue:
          temp = queue.popleft()

          for room in rooms[temp]:
            if room not in visited:
              queue.append(room)
              visited.add(room)

        return len(visited) == len(rooms)