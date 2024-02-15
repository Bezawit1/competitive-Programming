class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort()
        value = 0
        res = -1
        
        for num in nums:
            if num < value:
                res = num + value
            value += num
            
        return res
        
        