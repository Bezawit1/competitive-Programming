class Solution(object):
    def reductionOperations(self, nums):
        count = 0
        nums.sort(reverse = True)
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                count+=i+1
        return count
        
        