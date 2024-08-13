class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n , m = len(matrix) , len(matrix[0])
        for i in range(1,n):
            for j in range(m):
                left = matrix[i-1][j-1] if j > 0 else float('inf')
                middle = matrix[i-1][j]
                right = matrix[i-1][j+1] if j <m-1 else float('inf')
                matrix[i][j] +=min(left , middle , right)
        return min(matrix[-1])
            
        