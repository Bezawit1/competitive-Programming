class Solution(object):
    def applyOperations(self, nums):
        res =[]
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i]*=2
                nums[i+1]= 0
        for i in nums:
            if i > 0:
                res.append(i)
        while len(res) <len(nums):
            res.append(0)
        return res



        