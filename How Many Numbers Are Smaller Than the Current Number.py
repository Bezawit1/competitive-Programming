class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        sortednum =sorted(nums)
        hashmap={}
        res=[]
        for i in range(len(sortednum)):
            if sortednum[i] not in hashmap:
                hashmap[sortednum[i]]=i
        for i in range(len(nums)):
                res.append(hashmap[nums[i]])
            
        return res
