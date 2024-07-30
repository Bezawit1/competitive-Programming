class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
      
        n = len(graph)
        reversed_graph = defaultdict(list)
        out_degree = [0] * n
        
        for i in range(n):
            for j in graph[i]:
                reversed_graph[j].append(i)
                out_degree[i] += 1
        
        
        queue = deque()
        for i in range(n):
            if out_degree[i] == 0:
                queue.append(i)
        
        
        safe_nodes = []
        while queue:
            node = queue.popleft()
            safe_nodes.append(node)
            
           
            for neighbor in reversed_graph[node]:
                out_degree[neighbor] -= 1
                if out_degree[neighbor] == 0:
                    queue.append(neighbor)
       
        return sorted(safe_nodes)
        