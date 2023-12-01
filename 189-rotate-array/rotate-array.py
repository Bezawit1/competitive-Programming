class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
       
        if k !=0:
            remaining =nums [-k:]
            
            for i in range (len(nums)-k-1,-1,-1):
                nums[i+k] = nums[i]
       
            nums[:k] = remaining
        

