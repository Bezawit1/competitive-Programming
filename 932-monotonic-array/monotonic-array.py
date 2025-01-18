class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        stack = []
        if len(nums)<=2:
            return True
        stack.append(nums[0])
        stack.append(nums[1])
        for i in range(2 , len(nums)):
            if nums[i] > stack[-1] and stack[-1] < stack[0]:
                return False
            if nums[i] < stack[-1] and stack[-1] > stack[0]:
                return False
            stack.append(nums[i])
        return True


       
      
      

        