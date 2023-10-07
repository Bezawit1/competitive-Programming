class Solution(object):
    def sortColors(self, nums):

        countingArray = [0]*3
        for num in nums:
            countingArray[num]+=1
        index = 0
        for color in range(3): 
            for _ in range(countingArray[color]):
                nums[index] = color
                index += 1
        return nums
       
        