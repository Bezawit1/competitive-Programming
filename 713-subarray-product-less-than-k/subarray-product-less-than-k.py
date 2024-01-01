class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        i = 0
        j = 0 
        prod = 1
        count = 0
        while j < len(nums):
            prod *= nums[j]
            while prod >= k and i <= j:
                prod /= nums[i]
                i += 1
            
            
            count += (j - i + 1)

            j += 1
                
        return count
           

                


        