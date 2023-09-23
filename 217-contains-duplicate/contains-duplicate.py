class Solution(object):
    def containsDuplicate(self, nums):
        hashmap={}
        for i in nums:
            if i in hashmap:
                return True
            hashmap[i] = i
        return False

        
        