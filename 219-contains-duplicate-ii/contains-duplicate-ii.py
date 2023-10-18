class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        hashmap = {}
        
        for i in range(len(nums)):
            if nums[i] in hashmap and i - hashmap[nums[i]] <= k:
                return True
            hashmap[nums[i]] = i
        return False
          
                

       