class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        i = 0
        j = len(nums) - 1
        max_sum = 0
        while i <=j:
            max_sum = max(nums[i]+nums[j] ,max_sum)
            
            i+=1
            j-=1
        return max_sum
      

        