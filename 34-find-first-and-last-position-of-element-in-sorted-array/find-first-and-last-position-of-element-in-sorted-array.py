class Solution(object):
    def searchRange(self, nums, target):
        left  = 0 
        right = len(nums) - 1
        answer = [-1,-1]
        while left <= right:
            mid = left + (right - left) //2
            if nums[mid] > target :
                right = mid -1
            elif nums[mid] < target:
                left = mid + 1
            else:
                answer[0] = mid
                answer[1] = mid
                
                while answer[0] > 0 and nums[answer[0] - 1] == target:
                      answer[0] -= 1
                    
                while answer[1] < len(nums) - 1 and nums[answer[1] + 1] == target:
                    answer[1] += 1
                
                return answer
        return answer



       