class Solution(object):
    def numIdenticalPairs(self, nums):
        countPairs = 0
        for i in range(len(nums)):
            for j in range(i+1 ,len(nums) ):
                if nums[i] == nums[j]:
                    countPairs+=1
        return countPairs

        
        