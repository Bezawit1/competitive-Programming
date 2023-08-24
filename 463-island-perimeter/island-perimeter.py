class Solution(object):
    def islandPerimeter(self, grid):
        perimeter = 0
        row = len(grid)
        col = len(grid[0])
        for row_val in range(row):
            for col_val in range(col):
                cell=grid[row_val][col_val]
                if cell == 1:
                    if col_val == 0 or grid[row_val][col_val - 1] == 0:
                        perimeter += 1

                    if col_val == col - 1 or grid[row_val][col_val + 1] == 0:
                        perimeter += 1

                   
                    if row_val == 0 or grid[row_val - 1][col_val] == 0:
                        perimeter += 1

                    
                    if row_val == row - 1 or grid[row_val + 1][col_val] == 0:
                        perimeter += 1
        return perimeter
                    




       