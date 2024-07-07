class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        visited[0] = True
        queue = deque([0])
        while queue:
            current = queue.popleft()
            for i in rooms[current]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        return all(visited)
        
    

