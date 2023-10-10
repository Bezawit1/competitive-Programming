class Solution(object):
    def minOperations(self,nums):
      # sort the array and put it in a set to avoid duplicates
        unique_nums = sorted(set(nums))
        n = len(nums)
       
        j = 0
        min_ops = n
        for  i in range(len(unique_nums)):
            while j < len(unique_nums) and unique_nums[j] - unique_nums[i] <=len(nums) - 1:
                j+=1
                min_ops = min(min_ops , n -(j - i))
        return min_ops
    
            
            


        





       