class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        curr_prod =1
        j =0 
        i = 0
        count = 0
        while j < len(nums):
            curr_prod*=nums[j]
            
            
            while curr_prod >= k and i<=j:
                curr_prod/=nums[i]
                i+=1
            count+=(j-i + 1)
            j+=1
        return count
        