class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = nums[0]
        maxEnding = nums[0]

        for i in range(1, len(nums)):
       
            if nums[i] > nums[i - 1]:
                maxEnding += nums[i] 
            else:
                maxEnding = nums[i]  

            res = max(res, maxEnding)

        return res



        