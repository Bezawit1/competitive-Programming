class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph= defaultdict(list)
        incoming = [0]*n
        for node1 , node2 in edges:
            graph[node1].append(node2)
            incoming[node2]+=1
        
        queue = deque()
        res = [set() for _ in range(n)]
        for i in range(n):
            if incoming[i] == 0:
                queue.append(i)
        while queue:
            node = queue.popleft()
            
            for neigh in graph[node]:
               
                res[neigh].update(res[node])
                res[neigh].add(node)
                incoming[neigh] -= 1

                if incoming[neigh] == 0:
                    queue.append(neigh)
        
        
        result = [sorted(list(ancestors)) for ancestors in res]
        return result
        

        