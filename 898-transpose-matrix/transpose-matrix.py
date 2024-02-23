class Solution(object):
    def transpose(self, matrix):
        transposed = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
      
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                transposed[col][row] = matrix[row][col]
                
        return transposed
        
        