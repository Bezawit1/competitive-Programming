class Solution(object):
    def maximizeGreatness(self, nums):
        nums.sort()
        i = 0
        j = 0
        count = 0
        while j < len(nums):
            if nums[i] <nums[j]:
                count+=1
                i+=1
            j+=1
        return count
    
        