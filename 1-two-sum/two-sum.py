class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        arr=[]
        for i in range(0,len(nums)):
            complement = target- nums[i]
            if complement in hashmap:
                arr.append(hashmap[complement])
                arr.append(i)
            hashmap[nums[i]] = i
        return arr
           

       
        