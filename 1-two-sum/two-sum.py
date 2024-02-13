class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            difference = target - num
            if num in hashmap:
                return [hashmap[num], i]
            else:
                hashmap[difference] = i
        return []
       
        