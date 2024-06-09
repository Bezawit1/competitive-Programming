class Solution(object):
    def subsetsWithDup(self, nums):
        res = []
        nums.sort() 
        def backtracking(start, candidate):
            res.append(candidate[:])
            for i in range(start, len(nums)):
         
                if i > start and nums[i] == nums[i - 1]:
                    continue
                candidate.append(nums[i])
                backtracking(i + 1, candidate)
                candidate.pop()

        backtracking(0, [])
        return res
