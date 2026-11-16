class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        node_num = len(graph)
        colors = [0 for _ in range(node_num)]

        def dfs(node, color):
            for n in graph[node]:
                if colors[n] == color:
                    return False
                
                if colors[n] == 0:
                    colors[n] = -color 
                    
                    if not dfs(n, -color):
                        return False
            
            return True

        for i in range(node_num):
            if colors[i] == 0:
                colors[i] = 1 
                if not dfs(i, colors[i]): 
                    return False

        return True