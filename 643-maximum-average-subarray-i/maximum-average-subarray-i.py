class Solution(object):
    def findMaxAverage(self, nums, k):
        maxAvg = float('-inf')
        curr_sum = sum(nums[:k])

        for i in range(len(nums) - k + 1): 
            curr_avg = curr_sum / float(k)
            maxAvg = max(maxAvg, curr_avg)

            if i + k < len(nums):
                curr_sum -= nums[i]
                curr_sum += nums[i + k]

        return maxAvg



        
        