class Solution(object):
    def applyOperations(self, nums):
        i = 0
        j = len(nums) - 1
        newA = []

        for i in range(len(nums) - 1):
            
            if nums[i] != nums[i + 1]:
                continue
            else:
                nums[i] *= 2
                nums[i + 1] = 0
            

        for i in nums:
           if  i!=0:
               newA.append(i)
        while len(newA) < len(nums):
            newA.append(0)
            
        return newA

        
       


        
        