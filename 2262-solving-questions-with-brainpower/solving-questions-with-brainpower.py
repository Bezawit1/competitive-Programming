class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def dp(idx):
            if idx >= len(questions):
                return 0
            points, skip = questions[idx]
            solve = points + dp(idx + skip + 1)
            skip_question = dp(idx + 1)
            return max(solve, skip_question)
        
        return dp(0)

            
            
        