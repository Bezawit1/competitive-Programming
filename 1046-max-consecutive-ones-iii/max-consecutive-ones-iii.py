class Solution(object):
    def longestOnes(self, nums, k):
        i = 0
        maxlen = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                k -= 1
            while k < 0:
                if nums[i] == 0:
                    k += 1
                i += 1
            maxlen = max(maxlen, j - i + 1)
        return maxlen