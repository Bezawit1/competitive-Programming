class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        maxCount = 0
        for i in nums:
            if i == 0:
                count = 0
            else:
                count+=1
                maxCount = max(count , maxCount)
                
        return maxCount
        
        