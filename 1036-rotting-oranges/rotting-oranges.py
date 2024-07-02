class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


        if not grid:
            return -1
        
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque()
        fresh_count = 0
        minutes = 0
        
    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        
        if fresh_count == 0:
            return 0
        
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        fresh_count -= 1
            minutes += 1
        
   
        return minutes - 1 if fresh_count == 0 else -1

        