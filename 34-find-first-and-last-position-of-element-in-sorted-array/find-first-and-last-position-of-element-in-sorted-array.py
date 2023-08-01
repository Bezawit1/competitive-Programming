class Solution(object):
    def searchRange(self, nums, target):
        left, right = 0 ,len(nums) -1
        res=[]
        while left <= right:
            mid = left + (right - left ) //2
            if nums[mid] == target:
                start = mid
                end = mid
                while start > 0 and nums[start - 1] == target:
                    start -= 1
                while end < len(nums)-1 and nums [end + 1] == target:
                    end+=1
                return [start,end]
                
            elif nums[mid] < target:
                left+=1
            else:
                right-=1
        return [-1,-1]

        