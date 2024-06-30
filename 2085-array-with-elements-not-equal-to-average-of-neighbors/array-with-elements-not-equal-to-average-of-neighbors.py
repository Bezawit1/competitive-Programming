class Solution(object):
    def rearrangeArray(self, nums):
        nums.sort()
        result = []
        i, j = 0, len(nums) - 1
        
        while i < j:
            result.append(nums[i])
            result.append(nums[j])
            i += 1
            j -= 1
        
        if i == j:
            result.append(nums[i])
        
        return result
        