class Solution(object):
    def increasingTriplet(self, nums):
        first_min = float('inf')  
        next_min = float('inf') 
        
        for num in nums:
            if num <= first_min:
                first_min = num
            elif num <= next_min:
                next_min = num
            else:
                return True
        
        return False
        
        
    