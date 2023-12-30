class Solution(object):
    def divideArray(self, nums, k):
        nums.sort()
        hashmap = {}
        res = []
       
        # for i in nums:
        #     hashmap[i] = hashmap.get(i , 0)+ 1
     
        # # for element, frequency in hashmap.items():
        # #   if frequency > 3:
        # #     return []
        for i in range(0,len(nums)-2,3):
            diff = nums[i+2] - nums[i]
            
            if diff > k:
               return []
            else:
               res.append(nums[i:i+3])
           
        return res

        
            


      
    

        
    