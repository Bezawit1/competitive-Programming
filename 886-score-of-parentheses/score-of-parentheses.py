class Solution(object):
    def scoreOfParentheses(self, s):
        score = 0
        stack = []

        for char in s:
            if char == ")":
                score+=stack.pop() +max(score,1)
            else:
                stack.append(score)
                score=0
            

        return score
            