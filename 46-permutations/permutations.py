class Solution(object):
    def permute(self, nums):
        res = []
        def backtrack(start):
            if start == len(nums):
                res.append(nums[:])
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  
                backtrack(start + 1)  
                nums[start], nums[i] = nums[i], nums[start]  

        
        backtrack(0)
        return res