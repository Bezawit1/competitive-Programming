class NumMatrix:
    def __init__(self, matrix):
        if not matrix:
            return
        
        rows, cols = len(matrix), len(matrix[0])
        
        
        self.prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                self.prefix_sum[i][j] = (
                    matrix[i - 1][j - 1] +
                    self.prefix_sum[i - 1][j] +
                    self.prefix_sum[i][j - 1] -
                    self.prefix_sum[i - 1][j - 1]
                )
    
    def sumRegion(self, row1, col1, row2, col2):
        if not self.prefix_sum:
            return 0
        
        return (
            self.prefix_sum[row2 + 1][col2 + 1] -
            self.prefix_sum[row1][col2 + 1] -
            self.prefix_sum[row2 + 1][col1] +
            self.prefix_sum[row1][col1]
        )

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)