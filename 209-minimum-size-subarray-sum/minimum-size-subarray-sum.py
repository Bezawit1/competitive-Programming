class Solution(object):
    def minSubArrayLen(self, target, nums):
        i = 0 
        j = 0 
        curr_sum = 0
        minDis = float('inf')
        while  j < len(nums) and i < len(nums):
            curr_sum +=nums[j]
            print(curr_sum)
            while curr_sum >=target:
                  curr_sum-=nums[i]
                  minDis = min(minDis , j - i + 1)
                  i+=1
                  
                 
            j+=1
        return  0 if minDis == float('inf') else minDis


      

    
        