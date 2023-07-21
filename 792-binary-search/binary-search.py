class Solution(object):
    def search(self, nums, target):
        left,right = 0 , len(nums) - 1
        while left <= right:
            mid_index = left + (right - left)//2
            mid_val = nums[mid_index]
            if mid_val == target:
                return mid_index
            elif mid_val < target:
                left = mid_index + 1
            else:
                right = mid_index - 1
        return -1

        