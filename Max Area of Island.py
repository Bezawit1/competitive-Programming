class Solution(object):
    def maxAreaOfIsland(self, grid):
        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0 
            
        
            area = 1
            area += dfs(row + 1, col)
            area += dfs(row - 1, col)
            area += dfs(row, col + 1)
            area += dfs(row, col - 1)
            
            return area
    
        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    island_area = dfs(row, col)
                    max_area = max(max_area, island_area)
        
        return max_area
