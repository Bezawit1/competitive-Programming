class Solution(object):
    def runningSum(self, nums):
        running_sum = 0
        res =[]
        for i in nums:
            running_sum+=i
            res.append(running_sum)
        return res
        