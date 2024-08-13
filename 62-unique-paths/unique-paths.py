class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path = [1] * n

        for _ in range(m - 1):
            curr_path = [1] * n
            for i in range(1, n):
                curr_path[i] = curr_path[i-1] + path[i]
            path = curr_path
        
        return path[-1]
        