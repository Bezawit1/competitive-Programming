class Solution(object):
    def topKFrequent(self, nums, k):
        hashmap = {}
        res=[]
        for i in nums:
            hashmap[i] = hashmap.get(i,0) +1
        
        return [item[0] for item in sorted(hashmap.items(), key=lambda x: x[1], reverse=True)[:k]]


        
        