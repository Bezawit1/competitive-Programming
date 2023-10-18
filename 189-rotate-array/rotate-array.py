class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n  
        if k != 0: 
		end = nums[-k:]
		for i in range(n-k-1, -1, -1): 
			nums[i+k] = nums[i] 
		nums[:k] = end

   

         
        