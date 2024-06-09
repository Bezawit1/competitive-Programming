class Solution(object):
    def distributeCookies(self, cookies, k):
        res = [0] * k
        self.min_unfairness = float('inf')
        self.backtrack(0, cookies, res, 0)
        return self.min_unfairness
    
    def backtrack(self, start, cookies, res, max_fairness):
        if start == len(cookies):
            self.min_unfairness = min(self.min_unfairness, max_fairness)
            return
        
        for end in range(len(res)):
            res[end] += cookies[start]
            new_max_fairness = max(max_fairness, res[end])
           
            if new_max_fairness >= self.min_unfairness:
                res[end] -= cookies[start]
                continue
            self.backtrack(start + 1, cookies, res, new_max_fairness)
            res[end] -= cookies[start]
