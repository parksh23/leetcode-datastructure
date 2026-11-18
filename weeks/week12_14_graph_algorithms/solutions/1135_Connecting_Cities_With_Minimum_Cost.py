class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        if n == 1:
            return 0

        if len(connections) < n - 1:
            return -1

        connections.sort(key = lambda x : x[2])

        parents = list(range(n + 1))

        def find(x : int) -> int:
            if parents[x] != x:
                parents[x] = find(parents[x])

            return parents[x]

        def union(x : int, y : int) -> bool:
            parents_x, parents_y = find(x), find(y)

            if parents_x == parents_y:
                return False

            parents[parents_y] = parents_x

            return True

        cost_sum = 0
        num_edge = 0

        for u, v, cost in connections:
            if union(u, v):
                cost_sum += cost
                num_edge += 1
                if num_edge == n - 1:
                    return cost_sum

        return -1