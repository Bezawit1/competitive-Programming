class Solution(object):
    def isBipartite(self, graph):
      
        n = len(graph)
        colors = [0] * n 
        def dfs(node, color):
            colors[node] = color
            for i in graph[node]:
                if colors[i] == color:
                    return False
                if colors[i] == 0 and not dfs(i, -color):
                    return False
            return True
 
        for node in range(n):
            if colors[node] == 0 and not dfs(node, 1):
                return False
        return True

        