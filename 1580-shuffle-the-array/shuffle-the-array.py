class Solution(object):
    def shuffle(self, nums, n):
        i = 0
        j = n
        res = []
        while i < j and j < len(nums):
            res.append(nums[i])
            res.append(nums[j])
            i+=1
            j+=1
        return res


        
        