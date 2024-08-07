class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        currSum = nums[left]
        minLength = float('inf')
        while  right < len(nums):
            if currSum >= target:
                minLength = min(minLength, right - left + 1)
                currSum -= nums[left]
                left += 1
            else:
                right += 1
                if right < len(nums):
                    currSum += nums[right]
                        
        return minLength if minLength != float('inf') else 0
        