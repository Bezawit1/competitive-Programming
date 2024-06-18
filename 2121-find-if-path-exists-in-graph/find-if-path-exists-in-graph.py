class Solution(object):
    def validPath(self, n, edges, source, destination):
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        def dfs(node, visited):
            if node == destination:
                return True
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    if dfs(neighbour, visited):
                        return True
            return False
        
        return dfs(source, set())
      
        