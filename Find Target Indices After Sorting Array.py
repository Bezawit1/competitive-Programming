class Solution(object):
    def targetIndices(self, nums, target):
        idx=0
        nums = sorted(nums)
        res=[]
        for i in range(len(nums)):
            if nums[i]==target:
                res.append(i)
            
        return res
