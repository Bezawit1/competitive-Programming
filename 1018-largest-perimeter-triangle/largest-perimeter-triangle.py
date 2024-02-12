class Solution(object):
    def largestPerimeter(self, nums):
            nums.sort()
            maximum_sum = 0
            found = False
            
            for i in range(len(nums) - 2):
                if nums[i] + nums[i + 1] > nums[i + 2]:
                    found = True
                    maximum_sum = max(maximum_sum, nums[i] + nums[i + 1] + nums[i + 2])
            
            return maximum_sum if found else 0
        
        