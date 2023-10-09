class Solution(object):
    def minSubArrayLen(self, target, nums):
        i = 0
        j = 0
        minDis = float('inf')
        curr_sum = 0
        while j < len(nums):
            curr_sum +=nums[j]
            while curr_sum >= target:
                minDis = min(minDis, j - i + 1)
                curr_sum -= nums[i]
                i += 1
            j+=1
        return  0 if minDis == float('inf') else minDis

    
        