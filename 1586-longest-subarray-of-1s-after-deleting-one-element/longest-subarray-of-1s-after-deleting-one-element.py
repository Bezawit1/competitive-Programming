class Solution(object):
    def longestSubarray(self, nums):
      
        max_count = 0
        prev= 0
        current = 0

        for num in nums:
            if num == 1:
                current += 1
            else:
                prev= current
                current = 0

            max_count = max(max_count, prev+ current)

        if max_count == len(nums):
            return max_count - 1

        return max_count



        