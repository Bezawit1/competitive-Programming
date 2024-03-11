class Solution(object):
    def findDuplicate(self, nums):
        res={}
         
        for num in nums:
            if num in res:
               return num
            res[num] = 1
        
       
        return res
        
            
        