class Solution(object):
    def containsCycle(self, grid):
        def dfs(r, c, parent_r, parent_c):
            visited[r][c] = 1  
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == grid[r][c] and (nr != parent_r or nc != parent_c):
                    if visited[nr][nc] == 1:  
                        return True
                    elif visited[nr][nc] == 0: 
                        if dfs(nr, nc, r, c):
                            return True
            
            visited[r][c] = 2  
            return False

        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]  
        for r in range(m):
            for c in range(n):
                if visited[r][c] == 0:
                    if dfs(r, c, -1, -1):
                        return True

        return False

        
