class Solution(object):
    def minSubArrayLen(self, target, nums):
        min_len = float('inf')
        curr_sum = 0
        i = 0
        j = 0
        while j < len(nums):
            curr_sum+=nums[j]
            while curr_sum >= target:
                curr_sum-=nums[i]
                min_len= min(min_len,j-i+1)
                i+=1
            j+=1
        return 0 if min_len == float('inf') else min_len
           

       
        