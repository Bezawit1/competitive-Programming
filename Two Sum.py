class Solution(object):
    def twoSum(self, nums, target):
        hashM={}
        n=len(nums)
        for i in range(n):
            res = target-nums[i]
            if res in hashM:
                return [hashM[res],i]
            hashM[nums[i]]=i
        return []
