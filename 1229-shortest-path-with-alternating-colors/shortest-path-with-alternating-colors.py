from collections import deque, defaultdict

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        red_adj = defaultdict(list)
        blue_adj = defaultdict(list)
        
        for u, v in redEdges:
            red_adj[u].append(v)
        for u, v in blueEdges:
            blue_adj[u].append(v)
        
        
        queue_red = deque([(0, 0)])  
        queue_blue = deque([(0, 0)]) 
        
        dist_red = [float('inf')] * n 
        dist_blue = [float('inf')] * n 
        
        dist_red[0] = 0
        dist_blue[0] = 0
        
        
        while queue_red or queue_blue:
           
            while queue_red:
                node, distance = queue_red.popleft()
                for neighbor in red_adj[node]:
                    if distance + 1 < dist_blue[neighbor]:
                        dist_blue[neighbor] = distance + 1
                        queue_blue.append((neighbor, distance + 1))
            
            while queue_blue:
                node, distance = queue_blue.popleft()
                for neighbor in blue_adj[node]:
                    if distance + 1 < dist_red[neighbor]:
                        dist_red[neighbor] = distance + 1
                        queue_red.append((neighbor, distance + 1))
        
    
        answer = []
        for i in range(n):
            if dist_red[i] == float('inf') and dist_blue[i] == float('inf'):
                answer.append(-1)
            else:
                answer.append(min(dist_red[i], dist_blue[i]))
        
        return answer
