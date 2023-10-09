class Solution(object):
    def searchRange(self, nums, target):
        left  = 0 
        right = len(nums) - 1
        res = [-1,-1]
        while left <= right:
            mid = left + (right - left) //2
            if nums[mid] > target :
                right = mid -1
            elif nums[mid] < target:
                left = mid + 1
            else:
                res[0] = mid
                res[1] = mid
                
                while res[0] > 0 and nums[res[0] - 1] == target:
                      res[0] -= 1
                    
                while res[1] < len(nums) - 1 and nums[res[1] + 1] == target:
                    res[1] += 1
                
                return res
        return res



       