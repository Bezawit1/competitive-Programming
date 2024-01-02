class Solution(object):
    def minimumDifference(self, nums, k):
        nums.sort(reverse = True)
        minDiff = 10**5
        for i in range(len(nums) - k + 1):
            left = i
            right = i + k - 1
            
            minDiff = min(minDiff , nums[left] - nums[right])
        return minDiff


        
        