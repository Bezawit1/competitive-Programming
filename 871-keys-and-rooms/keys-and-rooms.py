class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        if not rooms:
            return False
        
        n = len(rooms)
        visited = [False] * n
        visited[0] = True
        queue = deque([0])
        
        while queue:
            current = queue.popleft()
            for key in rooms[current]:
                if not visited[key]:
                    visited[key] = True
                    queue.append(key)
        
        return all(visited)