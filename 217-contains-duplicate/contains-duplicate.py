class Solution(object):
    def containsDuplicate(self, nums):
        hashmap={}
        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
        for value in hashmap.values():
            if value >1 :
                return True
        return False
      