class Solution(object):
    def sortColors(self, nums):
        for i in range(len(nums)):
            for j in range(0,len(nums)-1):
                if nums[j] >nums[j+1]:
                    temp=nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1]=temp
        return nums
