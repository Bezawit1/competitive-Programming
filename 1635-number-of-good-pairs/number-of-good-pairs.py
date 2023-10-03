class Solution(object):
    def numIdenticalPairs(self, nums):
        hashmap={}
        good_pairs = 0
        for i in nums:
            hashmap[i] = hashmap.get(i,0)+1
        for count in hashmap.values():
            if count > 1:
                good_pairs += (count * (count - 1)) // 2
        
        return good_pairs

        