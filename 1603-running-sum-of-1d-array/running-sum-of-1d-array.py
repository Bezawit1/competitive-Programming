class Solution(object):
    def runningSum(self, nums):
        curr_sum = 0
        arr = []
        for i in nums:
            curr_sum +=i
            arr.append(curr_sum)
        return arr