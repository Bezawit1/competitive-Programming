class Solution(object):
    def moveZeroes(self, nums):
			i = 0
			j = 0
			while j < len(nums):
				if nums[j] != 0:
					nums[j], nums[i] = nums[i], nums[j]
					i+=1
				j+=1
			return nums

				
	
	    
			
		    
			    
		    
     
        

        