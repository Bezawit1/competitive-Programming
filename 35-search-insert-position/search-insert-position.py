class Solution(object):
    def searchInsert(self, nums, target):
        low,high = 0 , len(nums)-1
        while low <= high:
            mid_index=low+(high-low)//2
            mid_val=nums[mid_index]
            if mid_val == target:
                return mid_index
            elif mid_val < target:
                low = mid_index + 1
            else:
               high = mid_index - 1
        return low
       