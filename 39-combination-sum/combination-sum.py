class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        current = []

        def backTracking(start, curr_sum):
            if curr_sum == target:
                res.append(current[:]) 
                return
            elif curr_sum > target:
                return 

            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backTracking(i, curr_sum + candidates[i])
                current.pop() 

        backTracking(0, 0)
        return res
