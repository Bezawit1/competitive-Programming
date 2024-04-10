class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        window_start = window_end = 0
        for i in range(indexDifference, len(nums)):
            if nums[i - indexDifference] < nums[window_start]: 
                window_start = i - indexDifference
            if nums[i - indexDifference] > nums[window_end]: 
                window_end = i - indexDifference
            if nums[i] - nums[window_start] >= valueDifference: 
                return [window_start, i]
            if nums[window_end] - nums[i] >= valueDifference: 
                return [window_end, i]
        return [-1, -1]
