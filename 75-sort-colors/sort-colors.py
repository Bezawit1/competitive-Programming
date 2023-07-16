class Solution(object):
    def sortColors(self, nums):
        counters = [0]*3
        for num in nums:
            counters[num]+=1
        idx = 0
        for color in range(3):  # Iterate over the colors: 0, 1, and 2
            for _ in range(counters[color]):
                nums[idx] = color
                idx += 1
        return nums
        