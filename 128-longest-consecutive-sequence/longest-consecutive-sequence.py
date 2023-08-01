class Solution(object):
    def longestConsecutive(self, nums):
        hashmap={}
        count = 0
        for i in nums:
            currect_count=0
            hashmap[i] = hashmap.get(i,0)+1
        for num in nums:
            if num - 1 not in hashmap:
                current_count = 1
                while num + 1 in hashmap:
                    current_count += 1
                    num += 1
                count = max(count, current_count)
        return count
                
        