class Solution(object):
    def maximumDetonation(self, bombs):
        graph = defaultdict(list)
        for i , (xi, yi, ri) in enumerate(bombs):
            for j, (xj , yj ,rj) in enumerate(bombs):
                if (xi - xj) ** 2 + (yi - yj) ** 2 <= ri**2:
                    graph[i].append(j)
        def dfs(node , visited):
            for bomb in graph[node]:
                if bomb not in visited:
                    visited.add(bomb)
                    dfs(bomb , visited)
            return visited
        
        return max(len(dfs(i,set())) for i in range(len(bombs)))
        
        