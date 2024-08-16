class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def dp(idx: int, i: int) -> int:
            if i == len(t):
                return 1
            if idx >= len(s):
                return 0
            if s[idx] == t[i]:
                return dp(idx + 1, i + 1) + dp(idx + 1, i)
            return dp(idx + 1, i)
        
        return dp(0, 0)
