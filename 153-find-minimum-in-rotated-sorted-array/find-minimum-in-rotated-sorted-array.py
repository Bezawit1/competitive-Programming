class Solution(object):
    def findMin(self, nums):
        left = 0 
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            mid_element = nums[mid]
            if mid_element > nums[right]:
                left = mid + 1
            else:
                right = mid 
            

        return nums[left]

        