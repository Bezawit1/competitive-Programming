class Solution(object):
    def maxSubArray(self, nums):
        curr_sum = 0
        max_sum = float('-inf')
        for i in range(len(nums)):
            curr_sum = max(curr_sum + nums[i] , nums[i])
            max_sum = max(max_sum ,curr_sum)
        return max_sum

        