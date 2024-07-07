class Solution(object):
    def minDifference(self, nums):
        if len(nums) <=4:
            return 0
        nums.sort()
        min_diff = float('inf')
        
        for left in range(4):
            right = len(nums) - 4 + left
            min_diff = min(min_diff, nums[right] - nums[left])

        return min_diff
        
        
        