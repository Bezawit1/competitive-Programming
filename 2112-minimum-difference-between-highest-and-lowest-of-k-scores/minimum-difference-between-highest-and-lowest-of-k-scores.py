class Solution(object):
    def minimumDifference(self, nums, k):
        nums.sort()
        min_val = float('inf')
        window_size= len(nums) - k

        
        for i in range(window_size + 1):
            left = i
            right = i+k-1
            diff = nums[right] - nums[left]
            min_val = min(min_val, diff)
        
        return min_val
            