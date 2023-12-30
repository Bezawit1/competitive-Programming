class Solution(object):
    def divideArray(self, nums, k):
        nums.sort()
        res = []
       
        for i in range(0,len(nums)-2,3):
            diff = nums[i+2] - nums[i]
            
            if diff > k:
               return []
            else:
               res.append(nums[i:i+3])
           
        return res

        
            


      
    

        
    