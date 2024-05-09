class Solution(object):
    def search(self, nums, target):

        left = 0
        right = len(nums) -1
        while left<=right:
            mid_element =( left + right)//2
            if nums[mid_element] == target:
                return mid_element
            if nums[mid_element] < target:
                left = mid_element + 1
            else:
                right = mid_element - 1
        return -1

        
        