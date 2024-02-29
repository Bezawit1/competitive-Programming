class Solution(object):
    def sortColors(self, nums):
        count = [0]*3
        for num in nums:
            count[num]+=1
        idx = 0
        for color in range(3):
            for _ in range(count[color]):
                nums[idx] = color
                idx+=1
        return nums


        