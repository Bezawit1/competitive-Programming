class Solution(object):
    def topKFrequent(self, nums, k):
        hashmap={}
        res=[]
        for i in nums:
            hashmap[i]=hashmap.get(i,0) +1
        sorted_hashmap = sorted(hashmap.items() , key = lambda x:x[1] , reverse=True)
        for i in range(k):
            res.append(sorted_hashmap[i][0])
        return res
