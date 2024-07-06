class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count_pairs = 0
        col_map = {}
        for col in range(len(grid[0])):
            col_map[col] = []  
    
            for row in range(len(grid)):
                col_map[col].append(grid[row][col])
        
        for key , val in col_map.items():
            if val in grid:
               count_pairs+=grid.count(val)
        return count_pairs
       
            