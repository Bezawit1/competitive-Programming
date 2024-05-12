class Solution(object):
    def maximumCount(self, nums):
        max_count = 0
        left = 0
        right = len(nums) - 1
        pos_count =0
        neg_count =0
        zero_count = nums.count(0)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > 0:
                pos_count = len(nums) - mid
                right = mid - 1
                
            else:
               
                left = mid + 1
        
    
        neg_count = len(nums) - pos_count -zero_count
            
        return max(pos_count, neg_count)


        